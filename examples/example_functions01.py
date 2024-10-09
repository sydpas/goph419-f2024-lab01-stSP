import matplotlib.pyplot as plt

import numpy as np

from lab01.functions01 import (
    launch_angle_range,
)


def main():
    ve_v0 = 2.0   # Please input a number.
    alpha = 0.25  # Please input a number.
    tol_alpha = 0.04   # Please input a number.

    alpha_range = np.arange(0.01, 0.04)

    # Now we create two empty lists. One will store the minimum angles, and the other the maximum.
    min_angles = []
    max_angles = []

    for alpha in alpha_range:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        # This will add the first phi_range value.
        min_angles.append(phi_range)  # append the first (min) value
        max_angles.append(phi_range)  # append the last (max) value


    # Using the information above, we will create the plot.
    plt.xlabel("Altitude as a fraction of Earth's radius (meters)")
    plt.ylabel('Launch angle (radians)')

    plt.plot(alpha_range, min_angles)
    plt.plot(alpha_range, max_angles)

    plt.show()



if __name__ == "__main__":
    main()
