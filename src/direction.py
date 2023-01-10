
from collections import namedtuple

class Directions():
    vector_direction = namedtuple("vector_direction", "x y")
    NORTH = vector_direction(0,1)
    SOUTH = vector_direction(0,-1)
    WEST = vector_direction(-1,0)
    EAST = vector_direction(1,0)
    STOP = vector_direction(0,0) 

