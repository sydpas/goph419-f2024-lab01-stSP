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
    This function tests and compares the expected NumPy arcsin results vs. the actual results of the arcsin function
    created by this user.

    Parameter(s):
    -----
        None.

    Return(s):
    -----
        None.

    """

    tol = 1.0e-8  # Please enter the significant digit tolerance. The general tolerance is 1.0e-8.
    x = 1  # Please input an x value between -1 and 1 (inclusive) to generate results that do not raise a ValueError.

    print(f"Testing arcsin({x})...")

    # Expected output.
    expected = np.asin(x)

    # Actual output.
    actual = arcsin(x)

    # Compare results.
    if np.abs((actual - expected) / expected) < tol:
        print(f"Passed, the expected value matches the actual value of {actual}!")
    else:
        print(f"Failed, expected: {expected}, actual: {actual}")


def angletest():
    """
    Description of function:
    -----
    This function tests and compares the expected results of the launch angle function vs. the actual computed results
    in the function created by the user.

    Parameter(s):
    -----
        None.

    Return(s):
    -----
        None.

    """

    tol = 1.0e-8  # Please enter the significant digit tolerance. The general tolerance is 1.0e-8.
    ve_v0 = 2.0  # Please enter a ratio value.
    alpha = 0.25  # Please enter an alpha value.

    print(f"Testing launch_angle with a ve_v0 of ({ve_v0}) and an alpha of ({alpha})...")

    # Expected output.
    sin_phi = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * ve_v0 ** 2)))  # equation 17
    expected = np.asin(sin_phi)

    # Actual output.
    actual = launch_angle(ve_v0, alpha)

    # Compare results.
    if np.abs((actual - expected) / expected) < tol:
        print(f"Passed, the expected value matches the actual value of {actual}!")
    else:
        print(f"Failed, expected: {expected}, actual: {actual}")


def rangetest():
    """
    Description of function:
    -----
    This function tests and compares the expected results of the launch angle range function vs. the actual computed
    results in the function created by the user.

    Parameter(s):
    -----
        None.

    Return(s):
    -----
        None.

    """

    ve_v0 = 2.0  # Please enter a ratio value.
    alpha = 0.25  # Please enter an alpha value.
    tol_alpha = 0.024 # Please enter the alpha tolerance.

    print(f"Testing launch_angle_range with an alpha of ({alpha}) and a tol_alpha of ({tol_alpha})...")

    # Expected output.
    expected_list = []
    one_plus = ((1 + tol_alpha) * alpha)
    expected_list.append(launch_angle(ve_v0, one_plus))
    one_minus = ((1 - tol_alpha) * alpha)
    expected_list.append(launch_angle(ve_v0, one_minus))
    expected_range = np.array(expected_list)

    # Actual output.
    actual_range = np.array(launch_angle_range(ve_v0, alpha, tol_alpha))

    # Compare results.
    if np.array_equal(actual_range, expected_range):
        print(f"Passed, the expected range matches the actual range of {actual_range}!")
    else:
        print(f"Failed, expected: {expected_range}, actual: {actual_range}")


if __name__ == "__main__":
    astest(), angletest(), rangetest()
