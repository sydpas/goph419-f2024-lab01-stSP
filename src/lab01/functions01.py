import numpy as np


### STEP 1 ###
# make a function that
    # takes an input ratio of escape velocity:terminal velocity (ve_v0),
    # the desired max altitude as a fraction of Earth's radius (alpha)
    # and the tolerance for max altitude (tol_alpha)
# this function (launch_angle_range) should output a two component object (numpy.array) that contains
    # the min allowable launch angle when the max altitude is (1+tol_alpha)*alpha)
    # and the max allowable launch angle when the max altitude is (1-tol_alpha)*alpha)
# use equation 18 to compute the inverse sine so that 5 sig digs are correct.


def arcsin(x):
    pass
    # if -1 > x > 1, raise error!


def launch_angle(y):
    pass


def launch_angle_range(ve_v0,alpha,tol_alpha):
    """
    Description of function:
    -----

    Parameter(s):
    -----
        ve_v0: the input ratio of the escape velocity to terminal velocity.
        alpha: the desired maximum altitude as a fraction of Earth's radius.
        tol_alpha: the tolerance for maximum altitude.

    Return(s):
    -----
        phi_range:
    """

    #...
    # implementation of equations 17
    sinphi = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * (ve_v0)**2)))  # eq 17 step 1
    phi = np.arcsin(sinphi)
    phi_range = [phi]
    print(phi_range)
    # and 18
    #sinarc = np.arcsin
    #LHS_sin = np.square(arcsin)
    #...

    return phi_range

"""
sinphi = (1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * (ve_v0) ^ 2))   # eq 17 step 1
phi = np.arcsin(sinphi)     # eq 17 step 2

sinarc = np.arcsin
LHS_sin = np.square(arcsin)"""