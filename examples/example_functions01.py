import matplotlib.pyplot as plt

import numpy as np

from lab01.functions01 import (
    launch_angle_range,
)


def main():
    ve_v0 = 2.0   # Please input a number.
    alpha = 0.25  # Please input a number.
    tol_alpha = 0.04   # Please input a number.

    alpha_range = np.linspace(0.01, 0.04, 100)

    # Now we create two empty lists. One will store the minimum angles, and the other the maximum.
    min_angles = []
    max_angles = []

    for alpha in alpha_range:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[1])  # append the min value
        max_angles.append(phi_range[0])  # append the max value

    # Using the information above, we will create the plot.
    plt.xlabel("Alpha (meters)")
    plt.ylabel("Launch angle (radians)")

    plt.plot(alpha_range, min_angles, label = "Minimum angle", linewidth = 2, color = "green")  # Minimum angle.
    plt.plot(alpha_range, max_angles, label = "Maximum angle", linewidth = 2, color = "purple")  # Maximum angle.
    plt.legend(title = "Legend", alignment = "left")
    plt.title("Launch Angle as a Function of Altitude Relative to Earth's Radius")  # Y vs. x
    plt.savefig('C:\\Users\\sydne\\git\\goph419\\goph419-f2024-lab01-stSP\\figures\\launch_angle_vs_alpha.png')
    plt.show()


if __name__ == "__main__":
    main()

