import numpy


### STEP 1 ###
# make a function that
    # takes an input ratio of escape velocity:terminal velocity (ve_v0),

def ve_v0():
    ratio=float(input("Please enter the ratio of escape velocity to terminal velocity: "))
    return ratio

    # the desired max altitude as a fraction of Earth's radius (alpha)

def alpha():
    

    # and the tolerance for max altitude (tol_alpha)
# this function should output a two component object (numpy.array) that contains
    # the min allowable launch angle when the max altitude is (1+tol_alpha)*alpha)
    # and the max allowable launch angle when the max altitude is (1-tol_alpha)*alpha)
# use equation 18 to compute the inverse sine so that 5 sig digs are correct.

def launch_angle_range(ve_v0,alpha,tol_alpha):
    """description of function:

    parameters:
        ve_v0: the input ratio of the escape velocity to terminal velocity.
        alpha: the desired maximum altitude as a fraction of Earth's radius.
        tol_alpha: the tolerance for maximum altitude.
    return(s):
        phi_range:
    """

    #...
    # implementation of equations 17 and 18
    #...
    return phi_range