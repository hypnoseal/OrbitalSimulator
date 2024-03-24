import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Define the animate_simulation function to animate the trajectories of celestial bodies. 'trajectories' is a
# dictionary where key is the name of the celestial body and value is a list of (position, radius, color) tuples.
# 'animation_duration' is the desired duration of the animation in seconds.
def animate_simulation(trajectories, animation_duration):
    # Create a figure and axes with matplotlib
    fig, ax = plt.subplots()
    ax.set_xlim(-5e8, 5e8)  # Set the x-axis limits
    ax.set_ylim(-5e8, 5e8)  # Set the y-axis limits

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
    markers = {name: ax.plot([], [], 'o', markersize=10 * (trajectories[name][0][1] / max_radius), label=name,
                             color=[c / 255 for c in trajectories[name][0][2]])[0] for name in trajectories}

    # Function to initialize the animation
    # It sets the data of each marker to an empty list
    def init():
        for marker in markers.values():
            marker.set_data([], [])
        return markers.values()

    # Function to animate each frame, setting the x and y positions of each marker
    def animate(i):
        for name, marker in markers.items():
            if i < len(trajectories[name]):
                x, y = trajectories[name][i][0][:2]  # Safely extract x, y and ignore z if present
                marker.set_data(x, y)
        return markers.values()

    # Create the animation
    ani = animation.FuncAnimation(
        fig, animate, frames=total_frames, init_func=init, blit=True,
        interval=interval, repeat=False)

    plt.legend()

    print("Plotting animation...")
    print("Saving animation video...")
    ani.save('orbit_simulation.mp4', writer='ffmpeg', dpi=150)  # Save the animation as mp4 video file
    print("Animation video saved, showing animation!")
    plt.show()  # Display the animation
