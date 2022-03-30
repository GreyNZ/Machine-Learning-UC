import numpy as np

def linear_regression(ary1, ary2):
    """
    takes two numpy arrays as input:
    :param ary1: the first is the input part of the training data which is an m×n array (design matrix)
    :param ary2: the second is the output part of the training data which is a one-dimensional array (vector) with m elements
    :return: one-dimensional array (vector) θ, with (n + 1) elements, which contains the least-squares regression coefficients of the features; the first ("extra") value is the intercept.
    """

