'''
William Kostuch
Computational Physics Final Project
Collection of useful methods
'''

# Python packages
import numpy as np 
import vpython as vp 
# Import constants from main file
from main import dt, G
from .utilities import distance
from .celestials import create_planetesimal


def acceleration(A: vp.sphere, B: vp.sphere) -> vp.vec:
    """Returns the acceleration on A from B due to gravitational attraction.
        Note: returns a vp.vec object."""
    denom = vp.mag(A.pos - B.pos)**3
    if np.isclose(denom, 0):
        return vp.vec(1E20, 1E20, 1E20)
    return -G * B.mass * (A.pos - B.pos) / denom

def condense_asteroids(bodies: list) -> vp.sphere:
    """Averages the celestial bodies in bodies and returns a vp.sphere object."""
    # Starting values
    pos = vp.vec(0, 0, 0)
    mass = 0
    # Now loop through each item in bodies and combine it into the average
    for body in bodies:
        pos += body.pos 
        mass += body.mass 
    # Average the values and return a new asteroid object as the phantom object
    pos = pos / len(bodies)
    mass = mass / len(bodies)
    return create_planetesimal(pos=pos, mass=mass)

def get_accelerations(smalls: list, larges: list) -> np.ndarray:
    """Given a list of celestial bodies, returns a numpy array containing the 
        acceleration of each body due to the gravity of the other bodies."""
    acc_list = list()
    # Make a phantom body that is the average position and mass
    # for all of the small bodies
    asteroid_phantom = condense_asteroids(smalls) 
    # Loop through the list, computing the acceleration on each  small body
    # due to the large bodies
    for i,small in enumerate(smalls): #TODO: Look into turning this into multiple processes
        # Keep track of the acceleration, take into account the average
        # position and mass of all the other asteroids
        # But if this is updating star velocity, we don't want a phantom
        if smalls[0].type is 'star':
            acc = vp.vec(0, 0, 0)
        else:
            acc = acceleration(small, asteroid_phantom)
        for large in larges:
            # If the two objects are the same, skip it
            if small is large: 
                continue
            acc += acceleration(small, large)
        acc_list.append(acc/len(larges))
    return acc_list

def update_velocities(smalls: list, larges: list):
    """Updates the velocities of the celestial objects in bodies
        due to acceleration caused by gravitational attraction."""
    global dt
    accelerations = get_accelerations(smalls, larges)
    for i,body in enumerate(smalls):
        body.vel += accelerations[i]*dt
    return

def trim_collisions(smalls: list, larges: list):
    """Checks for and reconciles collisions between objects.
        If two large items collide, they'll join together.
        If two small items collide, they'll join together.
        If a small item collides with a large, the small will be
            absorbed by the large."""
    return

def update_positions(smalls: list, larges: list):
    """Updates the positions of the celestial objects in smalls and larges;
        takes into account current velocity and gravitational attraction."""
    global dt 
    update_velocities(smalls, larges)
    update_velocities(larges, larges)
    for small in smalls:
        small.pos += small.vel*dt 
    for large in larges:
        large.pos += large.vel*dt
    # Check for and handle any collisions between objects
    trim_collisions(smalls, larges)
