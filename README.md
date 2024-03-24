# Orbital Simulator

The Orbital Simulator project uses Python to simulate the motion of celestial bodies based on physics principles.

## Modules

The main modules in the project are:

### CelestialBody

This module defines the `CelestialBody` class. Each instance of the class represents a celestial body with the following properties:

- `name`: The name of the celestial body.
- `mass`: The mass of the celestial body.
- `position`: The initial position of the celestial body.
- `velocity`: The initial velocity of the celestial body.
- `radius`: The radius of the celestial body.
- `color`: The color to represent the celestial body in the visualization.

### Simulation

The `Simulation` class handles the physics simulation of the celestial bodies. It includes methods to calculate gravitational forces, update positions, and run the simulation.

Instances of the `Simulation` class contain a list of `celestial_bodies` which are simulated and a `trajectory` object to store the trajectory data.

### Constants and Config Loader

`constants.py` file contains all the necessary physical constants and conversion factors used in simulations.

`config_loader.py` is used to load the configuration for the simulation from a YAML file.

### Animator

The animator module is responsible for generating a visual representation of the simulation.

### Main.py

Main execution point of the program. Initializes the simulation and visualizer and starts the simulation.

## Running the Program

Ensure you have installed all necessary python packages (PyYAML, matplotlib, numpy, etc.) and then run `main.py`.

## Contributing

As this is a learning project, contributions in the form of suggestions, bug reports, or pull requests are welcome.

## License

This project is licensed under the MIT License, details of which can be found in `LICENSE.md`.