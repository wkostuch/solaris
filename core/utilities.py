'''
William Kostuch
Computational Physics Final Project
Various utility methods
'''
# Python packages
import numpy as np 
import vpython as vp 

def tuple_to_vec(t: tuple) -> vp.vec:
    """Converts a 3-dimensional tuple to a VPython vector."""
    return vp.vec(t[0], t[1], t[2])

def distance(a: vp.sphere, b: vp.sphere) -> float:
    """Returns the distance between two VPython spheres."""
    return vp.sqrt((a.pos.x - b.pos.x)**2
                    + (a.pos.y - b.pos.y)**2
                    + (a.pos.z - b.pos.z)**2)

