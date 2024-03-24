import yaml
import numpy as np
from models.celestial_body import CelestialBody


def load_configuration(config_path="celestial_config.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    celestial_bodies = {}
    for name, attributes in config['celestial_bodies'].items():
        mass = float(attributes['mass'])
        position = np.array(attributes['position'], dtype=np.float64)
        velocity = np.array(attributes['velocity'], dtype=np.float64)
        radius = float(attributes['radius'])
        color = tuple(map(int, attributes['color'].strip('()').split(',')))
        celestial_bodies[name] = CelestialBody(
            name=name,
            mass=mass,
            position=position,
            velocity=velocity,
            radius=radius,
            color=color
        )

    # Pack animation duration into a dictionary
    animation = {
        'duration': config.get('animation', {}).get('duration', 15)  # default to 15 seconds if not specified
    }

    # Pack simulation duration and timestep into a dictionary
    simulation = {
        'duration': config.get('simulation', {}).get('duration', 86400),  # default one day in seconds
        'timestep': config.get('simulation', {}).get('timestep', 600)  # default 10 minutes in seconds
    }

    return celestial_bodies, animation, simulation
