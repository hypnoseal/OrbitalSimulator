# In your main.py
from visualization.animator import animate_simulation
from simulation.simulator import Simulation
from utils.config_loader import load_configuration


def main():
    celestial_bodies, animation_config, simulation_config = load_configuration("orbital_simulator_config.yaml")

    sim = Simulation(celestial_bodies)
    sim.run_simulation(simulation_config['duration'], simulation_config['timestep'])

    animate_simulation(sim.trajectory, animation_config['duration'])


if __name__ == "__main__":
    main()
