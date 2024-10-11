import numpy as np

from lab01.functions01 import (
    arcsin,
    launch_angle,
    launch_angle_range,
)


def astest():
    """
    Description of function:
    -----

    Parameter(s):
    -----
        tol: error tolerance.
        x: ***

    Return(s):
    -----

    """

    tol = 1.0e-8
    x = 0.5  # Please input an x between -1 and 1 (inclusive).

    arcsin(x)

    # what is this test doing
    print(f"Testing arcsin({x})...")

    # expected output
    expected = np.asin(x)

    # actual output
    actual = arcsin(x)

    # compare results
    if np.abs((actual - expected) / expected) < tol:
        print(f"Passed, the expected value matches the actual value of {actual}!")
    else:
        print(f"Failed, expected: {expected}, actual: {actual}")


def angletest():
    """
    Description of function:
    -----

    Parameter(s):
    -----
        tol: error tolerance.
        x: ***

    Return(s):
    -----

    """

    tol = 1.0e-8
    ve_v0 = 2.0  # Please enter a ratio value.
    alpha = 0.3  # Please enter an alpha value.

    # what is this test doing
    print(f"Testing launch_angle with a ve_v0 of ({ve_v0}) and an alpha of ({alpha})...")

    # expected output
    sin_phi = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * ve_v0 ** 2)))  # eq 17 step 1
    expected = np.asin(sin_phi)

    # actual output
    actual = launch_angle(ve_v0, alpha)

    # compare results
    if np.abs((actual - expected) / expected) < tol:
        print(f"Passed, the expected value matches the actual value of {actual}!")
    else:
        print(f"Failed, expected: {expected}, actual: {actual}")


def rangetest():
    """
    Description of function:
    -----

    Parameter(s):
    -----

    Return(s):
    -----

    """

    ve_v0 = 2.0  # Please enter a ratio value.
    alpha = 0.25  # Please enter an alpha value.
    tol_alpha = 0.04  # Please enter the alpha tolerance.

    # what is this test doing
    print(f"Testing launch_angle_range with an alpha of ({alpha}) and a tol_alpha of ({tol_alpha})...")

    # expected output
    expected_list = []
    one_plus = ((1 + tol_alpha) * alpha)
    expected_list.append(launch_angle(ve_v0, one_plus))
    one_minus = ((1 - tol_alpha) * alpha)
    expected_list.append(launch_angle(ve_v0, one_minus))
    expected_range = np.array(expected_list)

    # actual output
    actual_range = np.array(launch_angle_range(ve_v0, alpha, tol_alpha))

    # compare results
    if np.array_equal(actual_range, expected_range):
        print(f"Passed, the expected range matches the actual range of {actual_range}!")
    else:
        print(f"Failed, expected: {expected_range}, actual: {actual_range}")


if __name__ == "__main__":
    astest(), angletest(), rangetest()
