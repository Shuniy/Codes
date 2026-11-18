# practice how svm works
# Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It tries to find the best boundary known as hyperplane that separates different classes in the data.

import numpy as np

def distance_from_boundary(x, weights, bias):
    # Calculate perpendicular distance
    # Do not use NumPy
    score = decision_function(x, weights, bias)
    numerator = abs(score)
    denominator = sum(w ** 2 for w in weights) ** 0.5
    return numerator / denominator

def decision_function(x, weights, bias):
    # Return the numerical score
    # Do not use NumPy
    s = 0
    for xi, wi in zip(x, weights):
        s += xi * wi
    return s + bias



def predict(x, weights, bias):
    # Return +1 or -1
    score = decision_function(x, weights, bias)
    return 1 if score >= 0 else -1


weights = [1, 1]
bias = -2.5
X = [
    [2, 2],
    [3, 2],
    [2, 3],
    [0, 0],
    [0, 1],
    [1, 0]
]

y = [1, 1, 1, -1, -1, -1]

print("Predictions:", [predict(x, weights, bias) for x in X])
