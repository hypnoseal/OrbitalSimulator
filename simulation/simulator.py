import numpy as np
from utils.constants import G  # Make sure this imports the gravitational constant


# Simulation class calculates the celestial bodies' positions as time progresses.
class Simulation:
    # Initializing Simulation class with given celestial bodies.
    # 'celestial_bodies' is a dictionary of celestial bodies participating in simulation.
    def __init__(self, celestial_bodies):
        self.celestial_bodies = celestial_bodies
        self.trajectory = {name: [] for name in celestial_bodies}

    # Implementing gravitational force calculation between two bodies. 'body1' and 'body2' are instances of the
    # celestial bodies. Calculate the force between them utilizing Newton's law of universal gravitation.
    def gravitational_force(self, body1, body2):
        r_vec = body2.position - body1.position  # Calculate the displacement vector from body1 to body2
        r_mag = np.linalg.norm(r_vec)  # Calculate the magnitude of the displacement vector
        r_hat = r_vec / r_mag  # Calculate the unit vector of the displacement

        # Newton's law of universal gravitation calculates the magnitude of the force F = G * (m1 * m2) / r^2 where G
        # is the gravitational constant, m1 and m2 are the masses of the bodies, r is the distance between them
        force_mag = G * body1.mass * body2.mass / r_mag ** 2

        # Converting the magnitude of the force into a vector with the direction of the unit vector.
        force_vec = force_mag * r_hat

        # The function then returns this force vector, which represents the gravitational force that body1
        # experiences due to body2
        return force_vec

    # Update the position and velocity of each celestial body according to the gravitational forces acting on them.
    # 'dt' is the time step for which the calculation is performed. This function uses Euler's method to approximate
    # the next position and velocity of a celestial body based on its current position, velocity, and the forces
    # acting upon it.
    def update_positions(self, dt):
        # First update the positions
        for name, body in self.celestial_bodies.items():
            force_sum = np.zeros(3)
            for other_name, other_body in self.celestial_bodies.items():
                if name != other_name:
                    force_sum += self.gravitational_force(body, other_body)
            # Euler's method for velocity: Δv = a*dt = (F/m)*dt where 'a' is the acceleration(force / mass in this
            # context), and 'dt' is a small time step. It approximates the new velocity by taking the old velocity
            # and adding the product of acceleration and the time step.
            body.velocity += force_sum / body.mass * dt
            # Euler's method for position: Δr = v*dt where 'v' is the velocity, and 'dt' is a small time step. It
            # approximates the new position by taking the old position and adding the product of the velocity and the
            # time step. # body.position += body.velocity * dt
            body.position += body.velocity * dt

        # Adjusting all bodies' positions to keep the first body at the origin
        primary_position = self.celestial_bodies[list(self.celestial_bodies.keys())[0]].position
        position_adjustment = np.zeros(3) - primary_position

        # Apply adjustment to all bodies
        for name, body in self.celestial_bodies.items():
            body.position += position_adjustment
            self.trajectory[name].append((body.position.copy(), body.radius, body.color))

    # Function to run simulation for a given total time.
    def run_simulation(self, total_time, dt):
        num_steps = int(total_time / dt)
        for _ in range(num_steps):
            self.update_positions(dt)
