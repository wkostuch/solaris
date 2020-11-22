'''
William Kostuch
Computational Physics Final Project
Main file for running the program
'''

# Python packages
import numpy as np 
import vpython as vp 
# Local imports
from core import celestials as celest
from core import utilities as ut
from core import movement as mov

'''
Constants for use by the various functions.
'''
# Constants for calculations
AU = 1.496E11 # Meters, distance from earth to sun
G = 6.67E-11  # Gravitational constant
AXIS_LENGTH = 2E11 
dt = 5E4    # Time step
# Limit constants denote the boundaries for the system,
# if an object goes out of bounds then we stop caring about it
X_LIMIT = AU
Y_LIMIT = AU 
Z_LIMIT = AU
# Lists for holding celestial objects
BODIES = list()
STARS = list()
PLANETESIMALS = list() 


def create_system(x_bound=15, y_bound=15, z_bound=15):
    """Creates the system to be simulated.  
        Objects that move outside of the bounds will be
        Discarded from the simulation."""
    # Set up the bounds on the system
    global X_LIMIT, Y_LIMIT, Z_LIMIT, AXIS_LENGTH
    X_LIMIT = x_bound * AU
    Y_LIMIT = y_bound * AU
    Z_LIMIT = z_bound * AU
    # Scale the axis length based on the size of the system
    AXIS_LENGTH = X_LIMIT / 10


if __name__ == "__main__":
    # Create the scene
    scene = vp.canvas(title = "Planet Formation", background = vp.color.black, 
                        width=1300, height=650)
    scene.autoscale = 1
    # Draw coordinate axes for reference
    x_axis = vp.curve(pos=[vp.vec(0,0,0), vp.vec(AXIS_LENGTH,0,0)], color=vp.vec(1,0,0))
    y_axis = vp.curve(pos=[vp.vec(0,0,0), vp.vec(0,AXIS_LENGTH,0)], color=vp.vec(0,1,0))
    z_axis = vp.curve(pos=[vp.vec(0,0,0), vp.vec(0,0,AXIS_LENGTH)], color=vp.vec(0,0,1))
    # Start populating the scene
    create_system(x_bound=15, y_bound=15, z_bound=15)
    bounds = (X_LIMIT, Y_LIMIT, Z_LIMIT)
    # Make some planetesimals
    for i in range(50):
        p = celest.create_random_planetesimal(bounds=bounds)
        PLANETESIMALS.append(p)
    # Make a binary system
    STARS = celest.create_binary_system(bounds=bounds)

    count = 0
    # Animate the simulation
    while True:
        if count % 200 is 0:
            print(f"Planetesimals: {len(PLANETESIMALS)}  |  Stars: {len(STARS)}")
            count = 0
        mov.update_positions(PLANETESIMALS, STARS)
        mov.bounding_box(PLANETESIMALS, bounds)
        mov.bounding_box(STARS, bounds)
        vp.rate(10)
        count += 1
