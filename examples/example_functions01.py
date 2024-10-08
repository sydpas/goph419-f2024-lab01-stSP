from lab01.functions01 import (
    launch_angle_range,
)


def main():
    ve_v0 = 2.0   # Please input a number.
    alpha = 0.25    # Please input a number.
    tol_alpha = 0.02   # Please input a number.

    launch_angle_range(ve_v0, alpha, tol_alpha)


if __name__ == "__main__":
    main()
