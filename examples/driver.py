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
    alpha = 0.25  # Please input a maximum altitude value.
    tol_alpha = 0.04   # Please input a value.

    # We need 2 graphs, one for x as alpha and one for x as ve_v0 to compare each to the launch angle.
    # First we will make x = ve_v0.

    # The Numpy linespace command creates an array with a specified amount of elements in a specific range.
    ve_v0_range = np.linspace(1.4, 2.0, 100)

    # Now we create two empty lists. One will store the minimum ve_v0, and the other the maximum.
    min_ve_v0 = []
    max_ve_v0 = []

    for ve_v0 in ve_v0_range:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_ve_v0.append(phi_range[0])  # This will append the minimum value.
        max_ve_v0.append(phi_range[1])  # This will append the maximum value.

    # Using the information above, we will create the plot.
    plt.figure(figsize=(10,6))
    plt.xlabel("Ve/V0 ratio")
    plt.ylabel("Launch angle (radians)")
    # Plotting the minimum ve_v0.
    plt.plot(ve_v0_range, min_ve_v0, label="Minimum Launch Angle", linewidth=2, color="#f67280")
    # Plotting the maximum ve_v0.
    plt.plot(ve_v0_range, max_ve_v0, label="Maximum Launch Angle", linewidth=2, color="#6c5b7b")
    plt.legend(title="Legend", alignment="left")
    plt.title("Launch Angle as a Function of the Ratio of Escape Velocity to Terminal Velocity")
    plt.savefig('C:\\Users\\sydne\\git\\goph419\\goph419-f2024-lab01-stSP\\figures\\launch_angle_vs_ve_v0.png')
    plt.show()

    # Now we will make x = alpha.

    # The recommended values are 0.01-0.04.
    alpha_range = np.linspace(0.01, 0.04, 100)

    # Again, we create two empty lists. One will store the minimum angles, and the other the maximum.
    min_angles = []
    max_angles = []

    for alpha in alpha_range:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[0])  # This will append the minimum value.
        max_angles.append(phi_range[1])  # This will append the maximum value.

    # Using the information above, we will create the plot.
    plt.figure(figsize=(10,6))
    plt.xlabel("Alpha (meters)")
    plt.ylabel("Launch angle (radians)")
    # Plotting the minimum angle.
    plt.plot(alpha_range, min_angles, label = "Minimum Launch Angle", linewidth = 2, color = "#495867")
    # Plotting the maximum angle.
    plt.plot(alpha_range, max_angles, label = "Maximum Launch Angle", linewidth = 2, color = "#c18c5d")
    plt.legend(title = "Legend", alignment = "left")
    plt.title("Launch Angle as a Function of Maximum Altitude Relative to Earth's Radius")
    plt.savefig('C:\\Users\\sydne\\git\\goph419\\goph419-f2024-lab01-stSP\\figures\\launch_angle_vs_alpha.png')
    plt.show()


if __name__ == "__main__":
    main()

