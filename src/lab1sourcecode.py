### STEP 1 ###
# make a function that
    # takes the ratio of escape velocity:terminal velocity (ve_v0),
    # the desired max altitude as a fraction of Earth's radius (alpha)
    # and the tolerance for max altitude (tol_alpha)
# this function should output a two component object (numpy.array) that contains
    # the min allowable launch angle when the max altitude is (1+tol_alpha)*alpha)
    # and the max allowable launch angle when the max altitude is (1-tol_alpha)*alpha)
# use equation 18 to compute the inverse sine so that 5 sig digs are correct.