'''
William Kostuch
Computational Physics Final Project
Various utility methods
'''
# Python packages
import numpy as np 
import vpython as vp 

# Constants
AU = 1.496E11

def tuple_to_vec(t: tuple) -> vp.vec:
    """Converts a 3-dimensional tuple to a VPython vector."""
    return vp.vec(t[0], t[1], t[2])

def distance(a: vp.sphere, b: vp.sphere) -> float:
    """Returns the distance between two VPython spheres."""
    return vp.sqrt((a.pos.x - b.pos.x)**2
                    + (a.pos.y - b.pos.y)**2
                    + (a.pos.z - b.pos.z)**2)

def collide(a: vp.sphere, b:vp.sphere) -> bool:
    """Returns a boolean stating if the spheres have collided."""
    return distance(a, b) <= (a.radius + b.radius)

def kill_bodies_at_indices(source: list, indices: list):
    """Removes the items in source at locations given by indices."""
    # Put the indices into descending order
    indices.reverse()
    for i in indices:
        # Set the object to be invisible and then delete it
        if i < len(source):
            source[i].visible = False
            del source[i]
    return 

def absorb(a: vp.sphere, b: vp.sphere):
    """Absorbs b into a due to collisions.
        Note: Performs conservation of momentum calculations on
        a and b."""
    # Conservation of momentum for the collision.
    new_mass = a.mass + b.mass 
    new_vel = (a.mass*a.vel + b.mass*b.vel) / new_mass
    # Set radius for stars
    if a.type is 'star' and b.type is 'star':
        new_radius = new_mass * (6.96E8 / 1.99E30)
    # Set radius for planetesimals
    if a.type is 'planetesimal' and b.type is 'planetesimal':
        new_radius = new_mass * (500 / 3.93E17) * 1E5
    # Update a with the new values 
    a.mass = new_mass
    a.vel = new_vel
    a.radius = new_radius

def average_distance_to_object(bodies: list, big_object: vp.sphere) -> float:
    """Returns the average distance from each body in bodies to big_object."""
    avg_distance = 0 
    for body in bodies:
        avg_distance += distance(body, big_object)
    avg_distance = avg_distance / len(bodies)
    return avg_distance / AU

def average_asteroid_mass(bodies: list) -> float:
    """Returns the average mass of the objects in bodies."""
    avg_mass = 0
    for body in bodies:
        avg_mass += body.mass 
    avg_mass = avg_mass / len(bodies)
    return avg_mass
