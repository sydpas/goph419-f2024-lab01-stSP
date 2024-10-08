import pytest

from lab01.functions01 import (
    arcsin,
    launch_angle,
    launch_angle_range,
)


def tests():
    """
    Description of function:
    -----
        
    """
    x = 0.9 # Please input a test x value. If
    if x < -1 or x > 1:
        raise ValueError(f"You have an invalid x value: {x}")
    else:
        arcsin(x)
        print(arcsin)

if __name__ == "__tests__":
    tests()