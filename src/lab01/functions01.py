import numpy as np

import math


# STEP 1 #
# make a function that
    # takes an input ratio of escape velocity:terminal velocity (ve_v0),
    # the desired max altitude as a fraction of Earth's radius (alpha)
    # and the tolerance for max altitude (tol_alpha)
# this function (launch_angle_range) should output a two component object (numpy.array) that contains
    # the min allowable launch angle when the max altitude is (1+tol_alpha)*alpha
    # and the max allowable launch angle when the max altitude is (1-tol_alpha)*alpha
# use equation 18 to compute the inverse sine so that 5 sig digs are correct.


def arcsin(x):
    if x < -1 or x > 1:
        raise ValueError(f"You have an invalid x value: {x}")
    # eq 18
    result = 0.0
    eps_a = 1.0
    tol = 1.e-8  # error tolerance
    n = 1
    fact_n = math.factorial(n)
    fact_2n = math.factorial(n*2)
    n_max = 100
    while eps_a > tol and n < n_max:
        dy = ((2 * x) ** (2 * n)) / ((n**2) * (fact_2n/(fact_n**2)))
        result += dy
        eps_a = abs(dy / result)  # error calc
        n += 1
        fact_n *= n
        fact_2n *= (2 * n) * ((2 * n) - 1)
    return np.sqrt(0.5*result)


def launch_angle(ve_v0, alpha):
    if ve_v0 < 0 or alpha < 0:
        raise ValueError(f"You have an invalid ratio or alpha value: {ve_v0}")
    # implementation of equations 17
    sin_phi = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * ve_v0**2)))  # eq 17 step 1
    result = arcsin(sin_phi)
    return result


def launch_angle_range(ve_v0, alpha, tol_alpha):
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
    array_list = []

    one_plus = ((1 + tol_alpha) * alpha)  # minimum allowable launch angle and max alt. new alpha
    array_list.append(launch_angle(ve_v0, one_plus))

    one_minus = ((1 - tol_alpha) * alpha)  # maximum allowable launch angle and min alt. new alpha
    array_list.append(launch_angle(ve_v0, one_minus))

    phi_range = np.array(array_list)
    return phi_range
