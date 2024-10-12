import numpy as np

import math


def arcsin(x):
    """
    Description of function:
    -----
    This function computes the inverse sine function.

    Parameter(s):
    -----
        x: value that is put in the inverse sine.

    Return(s):
    -----
        result: the inverse sine of x.
    """
    if x < -1 or x > 1:
        raise ValueError(f"You have an invalid x value: {x}")
    result = 0.0
    eps_a = 1.0
    tol = 1.e-8  # The significant digit tolerance. The general tolerance is 1.0e-8.
    n = 1
    fact_n = math.factorial(n)
    fact_2n = math.factorial(n*2)
    n_max = 100
    while eps_a > tol and n < n_max:
        # The implementation of equation 18 in the lab manual.
        dy = ((2 * x) ** (2 * n)) / ((n**2) * (fact_2n/(fact_n**2)))
        result += dy
        eps_a = abs(dy / result)  # This is the relative error calculation.
        n += 1
        fact_n *= n
        fact_2n *= (2 * n) * ((2 * n) - 1)
    return np.sqrt(0.5*result)


def launch_angle(ve_v0, alpha):
    """
    Description of function:
    -----
    This function takes an input ratio of escape velocity to terminal velocity and the desired maximum altitude as a fraction of Earth's radius, and uses equation 17 to compute the launch angle.

    Parameter(s):
    -----
        ve_v0: the input ratio of the escape velocity to terminal velocity.
        alpha: the desired maximum altitude as a fraction of Earth's radius.

    Return(s):
    -----
        answer: the launch angle.

    """
    if ve_v0 < 0 or alpha < 0:
        raise ValueError(f"You have an invalid ratio or alpha value.")
    # This is the implemenation of equation 17 from the lab manual.
    sin_phi = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * ve_v0**2)))
    # Using the arcsin(x) function to compute the arcsin of sin_phi.
    answer = arcsin(sin_phi)
    return answer


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Description of function:
    -----
    This function computes the minimum and maximum launch angle within the tolerance for maximum altitude, and outputs
     a 2-number array.

    Parameter(s):
    -----
        ve_v0: the input ratio of the escape velocity to terminal velocity.
        alpha: the desired maximum altitude as a fraction of Earth's radius.
        tol_alpha: the tolerance for maximum altitude.

    Return(s):
    -----
        phi_range: the 2 component array of the maximum and minimum launch angle.

    """

    # Creating an empty list to store the array values.
    array_list = []

    one_plus = ((1 + tol_alpha) * alpha)  # This will compute the minimum allowable launch angle at max altitude.
    array_list.append(launch_angle(ve_v0, one_plus))

    one_minus = ((1 - tol_alpha) * alpha)  # This will compute the maximum allowable launch angle at max altitude.
    array_list.append(launch_angle(ve_v0, one_minus))

    # Creating the array using the list.
    phi_range = np.array(array_list)

    return phi_range
