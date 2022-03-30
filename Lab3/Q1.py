import numpy as np


def linear_regression_1d(pairs):
    """
    fancy pantsy
    :param pairs: list of pairs (x,y): x = feature val, y = response val
    :return: pair (m, c) where m is the slope of the line of least squares fit, and c is the intercept of the line of least squares fit.
    """
    # m = (n x.y - ∑x ∑y) / (n x.x - (∑x)**2)
    # c = (∑y - m∑x)/n
    ary = np.asarray(pairs)
    sig_x, sig_y = np.sum(ary, axis=0)
    n = ary.shape[0]
    m = (n * np.dot(ary[:,0], ary[:,1]) - sig_x * sig_y) / (n * np.dot(ary[:,0], ary[:,0]) - (sig_x ** 2))
    c = (sig_y - m * sig_x) / n
    return (m, c)




data = [(1, 4), (2, 7), (3, 10)]
m, c = linear_regression_1d(data)
print(m, c)
print(4 * m + c)
