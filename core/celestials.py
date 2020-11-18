'''
William Kostuch
Computational Physics Final Project
Library for making different celestial objects
'''
# Python packages
import numpy as np 
import vpython as vp 
# Local packages
from .utilities import tuple_to_vec

# Constants
MASS_EARTH = 1.99E30
RADIUS_EARTH = 6.96E8
MASS_PLANETESIMAL = 3.93E17
RADIUS_PLANETESIMAL = 500

'''
STARS
'''

def create_star(pos=(0, 0, 0), mass=1.99E30, radius=6.96E8, 
                vel=(0, 0, 0), color=(1, 1, 0)) -> vp.sphere: 
    """Creates a star (vp.sphere object) with the specified parameters; 
        defaults to earth's sun."""
    return vp.sphere(pos = tuple_to_vec(pos), 
                    mass = mass,
                    radius = radius, 
                    vel = tuple_to_vec(vel),
                    color = tuple_to_vec(color),
                    type = 'star',
                    make_trail = True,
                    trail_type = 'curve',
                    interval = 10,
                    retain = 100,
                    trail_color = tuple_to_vec(color))

def create_random_star(bounds: tuple,) -> vp.sphere: 
    """Creates a random star.  
    # Arguments:
    - bounds (tuple): x, y, z boundaries for where the star should appear
        in space.
    - size (string): 'small', 'medium', or 'large'; corresponds to a small,
        medium, or large star.

    # Returns:
    - A vp.sphere object, located within bounds, with random attributes.
    """
    # Find a random spot in space within bounds
    pos = (int(np.random.randint(low=-10, high=10)*bounds[0]/10), 
                int(np.random.randint(low=-10, high=10)*bounds[1]/10), 
                int(np.random.randint(low=-10, high=10)*bounds[2]/10))
    # Random mass ranging from 0.1x the mass of the sun to 150x
    mass = int(np.random.randint(low=1, high=1500)/10) * 1.99E30
    # Tie the radius to the mass, based on the sun's radius and mass
    radius = mass * (6.96E8 / 1.99E30)
    # No velocity as the star is stationary
    vel = (0, 0, 0)
    # Random color
    color = (np.random.rand(), np.random.rand(), 0)
    return create_star(pos, mass, radius, vel, color)


'''
PLANETESIMALS
'''
    
def create_planetesimal(pos=(0, 0, 0), mass=3.93E17, radius=500, 
                vel=(0, 0, 0), color=(0.5, 0.5, 0.5)) -> vp.sphere:
    """Creates a planetesimal object, represented as a VPython sphere."""
    # Handle possible type issues
    if type(pos) is tuple:
        pos = tuple_to_vec(pos)
    if type(vel) is tuple:
        vel = tuple_to_vec(vel)
    return vp.sphere(pos = pos, 
                    mass = mass, 
                    radius = radius, 
                    vel = vel, 
                    color = tuple_to_vec(color),
                    type = 'planetesimal',
                    make_trail = True,
                    trail_type = 'curve',
                    interval = 5,
                    retain = 3,
                    trail_color = tuple_to_vec(color))

def create_random_planetesimal(bounds: tuple) -> vp.sphere:
    """Creates a random planetesimal.  
    # Arguments:
    - bounds (tuple): x, y, z boundaries for where the planetesimal should 
        appear in space.
    - size (string): 'small', 'medium', or 'large'; corresponds to a small,
        medium, or large planetesimal.

    # Returns:
    - A vp.sphere object, located within bounds, with random attributes.
    """
    # Find a random spot in space within bounds
    pos = (int(np.random.randint(low=-10, high=10)*bounds[0]/10), 
                int(np.random.randint(low=-10, high=10)*bounds[1]/10), 
                int(np.random.randint(low=-10, high=10)*bounds[2]/10))
    # Random mass ranging from 0.1x the mass of the default planetesimal to 15x
    mass = int(np.random.randint(low=1, high=150)/10) * 3.93E17
    # Tie the radius to the mass, based on the default radius and mass
    radius = mass * (500 / 3.93E17) * 1E5
    # Random velocity 
    vel = (np.random.rand()*1E4 * np.random.choice([1, -1]), 
            np.random.rand()*1E4 * np.random.choice([1, -1]), 
            np.random.rand()*1E4 * np.random.choice([1, -1])) #TODO: Check velocities
    # Gray color
    color = (0.5, 0.5, 0.5)
    return create_planetesimal(pos, mass, radius, vel, color)
