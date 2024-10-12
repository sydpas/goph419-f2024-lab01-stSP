import matplotlib.pyplot as plt

import numpy as np

from lab01.functions01 import (
    launch_angle_range,
)


def main():
    """
    Description of function:
    -----
    This function creates a graph using the 2-number array from the launch_angle_range(ve_v0, alpha, tol_alpha) in
    Matplotlib.

    Parameter(s):
    -----
        None.

    Return(s):
    -----
        None.

    """
    ve_v0 = 2.0   # Please input a value.
    alpha = 0.25  # Please input a value.
    tol_alpha = 0.04   # Please input a value.

    # The Numpy linespace command creates an array with a specified amount of elements in a specific range.
    alpha_range = np.linspace(0, 0.1, 100)

    # Now we create two empty lists. One will store the minimum angles, and the other the maximum.
    min_angles = []
    max_angles = []

    for alpha in alpha_range:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[1])  # This will append the minimum value.
        max_angles.append(phi_range[0])  # This will append the maximum value.

    # Using the information above, we will create the plot.
    plt.xlabel("Alpha (meters)")
    plt.ylabel("Launch angle (radians)")
    # Plotting the minimum angle.
    plt.plot(alpha_range, min_angles, label = "Minimum angle", linewidth = 2, color = "#495867")
    # Plotting the maximum angle.
    plt.plot(alpha_range, max_angles, label = "Maximum angle", linewidth = 2, color = "#c18c5d")
    plt.legend(title = "Legend", alignment = "left")
    plt.title("Launch Angle as a Function of Altitude Relative to Earth's Radius")
    plt.savefig('C:\\Users\\sydne\\git\\goph419\\goph419-f2024-lab01-stSP\\figures\\launch_angle_vs_alpha.png')
    plt.show()


if __name__ == "__main__":
    main()

