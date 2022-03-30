# -*- coding: utf-8 -*-
"""COSC401 Machine Learning Linear Models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dqJKxPQnO-hy2iLox4zrnpeWQOrFRSf2

#Q1 . . Linear regression
"""

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

"""# Q2 . . Linear regression"""

import numpy as np

def linear_regression(xs, ys):
  """
  takes two numpy arrays as input: 
  xs: training data which is an m×n array (design matrix), 
  ys: output part of the training data which is a one-dimensional array (vector) with m elements
  Returns: one-dimensional array (vector) θ, with (n + 1) elements, 
  which contains the least-squares regression coefficients of the features; the first ("extra") value is the intercept.
  """
  # Theta = (X.T * X)^(-1) * X.T * y
  xs2 = np.insert(xs, 0, np.ones(xs.shape[0]), axis=1)
  #print(xs2)
  result = np.dot(np.dot(np.linalg.inv(np.dot(xs2.T, xs2)), xs2.T), ys)
  return result

xs = np.arange(5).reshape((-1, 1))   #[[0][1][2][3][4]]
ys = np.arange(1, 11, 2) #[1 3 5 7 9]
print(linear_regression(xs, ys)) # Should be [1. 2.]

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8]).T
print(linear_regression(xs, ys)) # Should be [-1.  2.  1.]

xs = np.array([[0, 1, 2, 3, 4],
               [0, 1, 4, 9, 16]]).T
ys = np.array([3, 6, 11, 18, 27]).T
print(linear_regression(xs, ys)) # Should be [3. 2. 1.]

"""# Q3  . .         Linear regression with basis functions"""

def linear_regression(xs, ys, basis_functions=None):
  """
  xs (training input), 
  ys (training output), 
  basis_functions which is a list of basis functions 
  Returns: one-dimensional array coefficients, first elements is the offset. rest are coefficients of corresponding basis functions
  Return: [Offset, coef_a, coef_b, .....]
  """
  if basis_functions is not None:
    xs2 = np.ones(xs.shape[0]).reshape(-1, 1)
    for func in basis_functions:
      xs2 = np.insert(xs2, xs2.shape[1], np.apply_along_axis(func, 1, xs), axis=1)
  else:
    xs2 = np.insert(xs, 0, np.ones(xs.shape[0]), axis=1)
  result = np.dot(np.dot(np.linalg.inv(np.dot(xs2.T, xs2)), xs2.T), ys)
  return result

xs = np.arange(5).reshape((-1, 1)) # [0 1 2 3 4]
ys = np.array([3, 6, 11, 18, 27])  # [3, 6, 11, 18, 27]
# Can you see y as a function of x? [hint: it's quadratic.]
functions = [lambda x: x[0], lambda x: x[0] ** 2]
#functions = []
print(linear_regression(xs, ys, functions))

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8]).T
print(linear_regression(xs, ys)) # Should be [-1.  2.  1.]

xs = np.arange(5).reshape((-1, 1)) # [0 1 2 3 4]
ys = np.array([3, 6, 11, 18, 27])  # [3, 6, 11, 18, 27]
# Can you see y as a function of x? [hint: it's quadratic.]
functions = [lambda x: x[0], lambda x: x[0] ** 2]
print(linear_regression(xs, ys, functions))

"""#Q4 . . Regularisation"""

import numpy as np

def linear_regression(xs, ys, basis_functions=None, penalty=0):
  """
  xs (training input), 
  ys (training output), 
  basis_functions which is a list of basis functions 
  penalty optional float penalty and returns the ridge regression coefficients.
  Returns: one-dimensional array coefficients, first elements is the offset. rest are coefficients of corresponding basis functions
  Return: [Offset, coef_a, coef_b, .....]
  """
  if basis_functions is not None:
    xs2 = np.ones(xs.shape[0]).reshape(-1, 1)
    for func in basis_functions:
      xs2 = np.insert(xs2, xs2.shape[1], np.apply_along_axis(func, 1, xs), axis=1)
  else:
    xs2 = np.insert(xs, 0, np.ones(xs.shape[0]), axis=1)
  result = np.dot(np.dot(np.linalg.inv(np.dot(xs2.T, xs2) + penalty * np.eye(xs2.shape[1])), xs2.T), ys)
  return result

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)

print(linear_regression(xs, ys), end="\n\n")

with np.printoptions(precision=5, suppress=True):
    print(linear_regression(xs, ys, penalty=0.1))

# SHOULD GET
#
# [1. 2.]
#
# [0.98113 1.99963]

import numpy as np

# we set the seed to some number so we can replicate the computation
np.random.seed(0)

xs = np.arange(-1, 1, 0.1).reshape(-1, 1)
m, n = xs.shape
# Some true function plus some noise:
ys = (xs**2 - 3*xs + 2 + np.random.normal(0, 0.5, (m, 1))).ravel()

functions = [lambda x: x[0], lambda x: x[0]**2, lambda x: x[0]**3, lambda x: x[0]**4,
      lambda x: x[0]**5, lambda x: x[0]**6, lambda x: x[0]**7, lambda x: x[0]**8]

for penalty in [0, 0.01, 0.1, 1, 10]:
    with np.printoptions(precision=5, suppress=True):
        print(linear_regression(xs, ys, basis_functions=functions, penalty=penalty)
              .reshape((-1, 1)), end="\n\n")

"""#Q5 . . Logistic regression"""

import numpy as np
import math

def logistic_regression(xs, ys, alpha, num_iterations):
  """
  xs (training input), 
  ys (training output), 
  alpha parameter is the training/learning rate
  num_iterations is the number of iterations (times to loop over the entire dataset)

  return: a model, must be a callable object (function) that accepts a one-dimensional array (vector) of values,
          and produces a value between 0 and 1 indicating the probability of that input vector belonging to the positive class.
  """
  sigmoid = lambda x: 1 / (1 + math.exp(-x))
  num_examples, num_features = xs.shape
  coeff = np.zeros(num_features)

  for iteration in range(num_iterations):
      z = np.dot(xs, coeff)
      print(z) # this should be a value now
      prediction = sigmoid(z)
      error = ys - prediction
      gradient = np.dot(xs.T, error)
      coeff = coeff + alpha * gradient

  def predict(test_inputs):
      z = np.dot(test_inputs, coeff)
      probs = sigmoid(z)
      return probs

  return predict

def logistic_regression(xs, ys, alpha, num_iterations):
    """
    xs (training input),
    ys (training output),
    alpha parameter is the training/learning rate
    num_iterations is the number of iterations (times to loop over the entire dataset)

    return: a model, must be a callable object (function) that accepts a one-dimensional array (vector) of values,
            and produces a value between 0 and 1 indicating the probability of that input vector belonging to the positive class.
    """

    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    num_examples, num_features = xs.shape
    coef = 0

    for iteration in range(num_iterations):
        print(iteration)
        for _xs, _y in zip(xs, ys):
            z = coef * _xs[0]
            pred = sigmoid(z)
            error = _y - pred
            gradient = _xs[0] * error
            #print(f'init coef: {coef}')
            #print(f'pred: {pred}')
            #print(f'error: {error}')
            print(f'gradient: {gradient}')
            coef += alpha * gradient
            print(f'new  coef: {coef}')

        #coef = coef + alpha * np.dot(xs.T, ys - sigmoid(np.dot(xs, coef)))

    def predict(test_inputs):
        z = np.dot(test_inputs, coef)
        probs = [sigmoid(ti*coef) for ti in test_inputs]
        return probs

    return predict

xs = np.array([1, 2, 3, 101, 102, 103]).reshape((-1, 1))
ys = np.array([0, 0, 0, 1, 1, 1])
model = logistic_regression(xs, ys, 0.05, 10000)
test_inputs = np.array([1.5, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101.8, 97]).reshape((-1, 1))

for test_input in test_inputs:
    print("{:.2f}".format(np.array(model(test_input)).item()))

import numpy as np
import math

def logistic_regression(xs, ys, alpha, num_iterations):
    """
    xs (training input),
    ys (training output),
    alpha parameter is the training/learning rate
    num_iterations is the number of iterations (times to loop over the entire dataset)

    return: a model, must be a callable object (function) that accepts a one-dimensional array (vector) of values,
            and produces a value between 0 and 1 indicating the probability of that input vector belonging to the positive class.
    """

    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    intercept = 0
    coef = 0

    for iteration in range(num_iterations):
        #print(iteration)
        for _xs, _y in zip(xs, ys):
            z = intercept + coef * _xs[0]
            pred = sigmoid(z)
            error = _y - pred
            gradient = _xs[0] * error
            #gradient = (_y  - pred) * pred * (1 - pred) * _xs[0]
            coef += alpha * gradient

            #intercept += alpha * (_y  - pred) * pred * (1 - pred)
            intercept += alpha * error

        #coef = coef + alpha * np.dot(xs.T, ys - sigmoid(np.dot(xs, coef)))

    def predict(test_inputs):
        probs = np. array([sigmoid(intercept + ti*coef) for ti in test_inputs])
        return probs

    return predict

xs = np.array([1, 2, 3, 101, 102, 103]).reshape((-1, 1))
ys = np.array([0, 0, 0, 1, 1, 1])
model = logistic_regression(xs, ys, 0.05, 10000)
test_inputs = np.array([1.5, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101.8, 97]).reshape((-1, 1))

for test_input in test_inputs:
    print("{:.2f}".format(np.array(model(test_input)).item()))

xs = np.array(
    [0.50,0.75,1.00,1.25,1.50,
     1.75,1.75,2.00,2.25,2.50,
     2.75,3.00,3.25,3.50,4.00,
     4.25,4.50,4.75,5.00,5.50]).reshape((-1, 1))

ys = np.array([0,0,0,0,0,
               0,1,0,1,0,
               1,0,1,0,1,
               1,1,1,1,1])

model = logistic_regression(xs, ys, 0.02, 5000)
sse = 0
output = []
expected = [0.02, 0.03, 0.07, 0.14, 0.25, 0.42, 0.60, 0.77, 0.87, 0.94, 0.97, 0.99]
for i, x in enumerate(np.arange(0, 6, 0.5).reshape(-1,1)): 
    output.append(np.array(model(x)).item())
    sse += (expected[i] - output[-1]) ** 2

tolerance = 1e-3
if sse / len(expected) < tolerance:
    print("OK")
else:
    print("The error is too high.")
    print("The expected output is: ", expected)

data = np.genfromtxt("data_banknote_authentication.txt", delimiter=',')
np.random.seed(0)
np.random.shuffle(data)
data = data[:500, :]

xs_train, xs_test = data[:-50, :-1], data[-50:, :-1]
ys_train, ys_test = data[:-50, -1], data[-50:, -1]
model = logistic_regression(xs_train, ys_train, 0.02, 1000)
print(sum(abs(y - model(x)) for (x, y) in zip(xs_test, ys_test))/50 < 0.05)