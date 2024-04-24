import numpy as np

def gradient_descent(x, y):
    m = b = 0          # m is the slope and b is the intercept...
    iterations = 100
    n = len(x)
    learning_rate = 0.0001
    for i in range(iterations):
        y_predicted = m*x + b
        cost = (1/n) * sum({val**2 for val in (y-y_predicted)})
        m_derivative = -(2/n)*sum(x*(y - y_predicted))
        b_derivative = -(2/n)*sum(x*(y - y_predicted))
        m = m - learning_rate*m_derivative
        b = b - learning_rate*b_derivative
        print("m {}, b {}, cost {}, iteration {}".format(m, b, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)