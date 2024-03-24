"""
This Python file is designed to define and represent celestial bodies in the simulation.
It includes classes, methods, and operations necessary for simulating the behavior
and interaction of celestial bodies in a predefined universe.
"""


# Class definition of the Celestial Body
class CelestialBody:
    def __init__(self, name, mass, position, velocity, radius, color):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color
