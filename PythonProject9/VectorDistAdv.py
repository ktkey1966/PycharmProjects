# Ex. 15 Vector Distance
# Kevin Key
# 11/13/2025

"""
You are given an array x_train with multiple input vectors ("training data") and another
array x_test ("test data"). Write a code that finds the vector in x_train is closest to
each vector in x_test. Find the nearest neighbor for each vector in x_test.
"""


import numpy as np

x_train = np.random.rand(10, 3)     # Generate 10 random vectors of size 3
x_test = np.random.rand(3)          # Generate 1 test vector of size 3

# Distance function
def dist(a, b):
    total = 0
    for ai, bi in zip(a, b):
        total += (ai - bi) ** 2
    return np.sqrt(total)

def nearest(x_train, x_test):
    nearest_index = -1
    min_distance = np.inf

    # Loop through each vector in x_train
    for i in range(len(x_train)):
        # Calculate the distance between x_train[i] and x_test
        d = dist(x_train[i], x_test)

    # Check if the distance is smaller than the current minimum distance
        if d < min_distance:
            min_distance = d
            nearest_index = i

    print(nearest_index)
    return nearest_index

nearest(x_train, x_test)




