import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


# Define the animate_simulation function to animate the trajectories of celestial bodies. 'trajectories' is a
# dictionary where key is the name of the celestial body and value is a list of (position, radius, color) tuples.
# 'animation_duration' is the desired duration of the animation in seconds.
def animate_simulation(trajectories, hamiltonians, animation_duration):
    # Create 3D figure and axes with matplotlib
    fig = plt.figure(facecolor='black')
    ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=7, projection='3d', fig=fig)
    ax2 = plt.subplot2grid((8, 1), (7, 0), rowspan=1, fig=fig)

    # Set up orbit plot
    ax1.set_facecolor('black')
    ax1.grid(False)
    ax1.axis('off')

    ax1.set_xlim(-2.5e8, 2.5e8)  # Set the x-axis limits
    ax1.set_ylim(-2.5e8, 2.5e8)  # Set the y-axis limits
    ax1.set_zlim(-2.5e8, 2.5e8)  # Set the z-axis limits
    ax1.view_init(elev=10, azim=45)  # Set the perspective

    # Add Hamiltonian energy changes plot
    # Calculate magnitude of Hamiltonian vectors
    magnitude = np.linalg.norm(hamiltonians[0])

    ax2.set_facecolor('black')
    ax2.set_title('Hamiltonian Energy Changes', color='white')
    ax2.set_ylabel('Energy [Joules]', color='white')
    ax2.set_xlabel('Time', color='white')
    ax2.grid(color='white', linestyle='-', linewidth=0.1)
    ax2.tick_params(colors='white')
    for spine in ax2.spines.values():
        spine.set_edgecolor('white')
    magnitude_line, = ax2.plot([], [], color='green', label='Magnitude')  # Line to plot magnitude

    # Determine which celestial body has the most trajectory points
    # The 'max' function is used with a key argument that returns the lengths of each trajectory
    max_trajectory = max(trajectories, key=lambda k: len(trajectories[k]))
    total_frames = len(trajectories[max_trajectory])

    # Adjust the interval to speed up or slow down the animation
    # It converts the animation_duration to milliseconds and divides it by the number of total frames
    interval = max(int(animation_duration / total_frames * 1000), 1)

    # Calculate the maximum radius among all celestial bodies to normalize the markersize of each body
    max_radius = max([max([radius for (_, radius, _) in trajectories[name]]) for name in trajectories])

    # Prepare moving markers for each celestial body
    # 'markersize' is scaled based on the current celestial body's radius and the maximum radius
    # The color of the marker is specified using the RGB color code in the trajectories data
    markers = {name: ax1.plot([], [], [], 'o', markersize=10 * (trajectories[name][0][1] / max_radius), label=name,
                             color=[c / 255 for c in trajectories[name][0][2]])[0] for name in trajectories}
    lines = {name: ax1.plot([], [], [], color='white', label=None)[0] for name in trajectories}


    # Function to initialize the animation
    # It sets the data of each marker to an empty list
    def init():
        for marker in markers.values():
            marker.set_data([], [])
            marker.set_3d_properties([])
        for line in lines.values():
            line.set_data([], [])
            line.set_3d_properties([])
        return markers.values(), lines.values()

    # Function to animate each frame, setting the x, y, and z positions of each marker
    def animate(i):
        for name in markers.keys():
            if i < len(trajectories[name]):
                x, y, z = trajectories[name][i][0]
                markers[name].set_data(x, y)
                markers[name].set_3d_properties(z)
                if i > 0:
                    prev_x, prev_y, prev_z = trajectories[name][i - 1][0]
                    lines[name].set_data([prev_x, x], [prev_y, y])
                    lines[name].set_3d_properties([prev_z, z])

        magnitude_line.set_data(range(i + 1), [magnitude] * (i + 1))  # Plot Hamiltonian magnitude
        ax2.relim()
        ax2.autoscale_view()

        return markers.values(), lines.values()

    # Create the animation
    ani = animation.FuncAnimation(
        fig, animate, frames=total_frames, init_func=init, interval=interval, repeat=False)
    leg = ax1.legend(loc='upper right')
    leg.get_frame().set_alpha(None)
    leg.get_frame().set_facecolor('black')
    leg.get_frame().set_edgecolor('none')
    for text in leg.get_texts():
        text.set_color('white')
    ax2.legend().remove()

    print("Plotting animation...")
    print("Saving animation video...")
    ani.save('orbit_simulation.mp4', writer='ffmpeg', dpi=150)  # Save the animation as mp4 video file
    print("Animation video saved, showing animation!")
    plt.show()  # Display the animation
