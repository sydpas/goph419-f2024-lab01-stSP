import numpy as np

from lab01.functions01 import (
    launch_angle_range,
)

"""constants:
earth radius: earth radius in meters (1.56786e-7).
"""


def main():
    ve_v0 = 2.0   # Please input a number.
    alpha = 0.15    # Please input a number.
    tol_alpha = 0.01    # Please input a number.

    one_plus = ((1 + tol_alpha) * alpha)
    one_minus = ((1 - tol_alpha) * alpha)
    nu_ar = np.array([one_plus, one_minus])
    print(nu_ar)

    arcsin(x)
    launch_angle(y)
    launch_angle_range(ve_v0, alpha, tol_alpha)


if __name__ == "__main__":
    main()
