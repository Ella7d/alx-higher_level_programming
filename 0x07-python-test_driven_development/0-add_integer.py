#!/usr/bin/python3
"""Define addition of two integers"""

def add_integer(a, b=98):
    """Return integer of a and b.
    
    If float typecast into integers.
    
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """
    if((not isininstance(a, int) and isininstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isininstance(b, int) and isininstance(b, float))):
        raise TypeError("b must be an integer")
        return(int(a) + int(b))

