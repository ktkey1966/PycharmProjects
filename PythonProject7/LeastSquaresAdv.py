# Ex. 12 Least Squares Advance
# Kevin Key
# 10/29/2025

import numpy as np

# Data: each row is one cabin, columns are features
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])

# Actual prices for the three cabins
y = np.array([250000, 60000, 525000])

# Alternative sets of coefficient values
C = np.array([[3000, 200, -50, 5000, 100],
              [2000, -150, -100, 150, 250],
              [3000, -100, -150, 0, 150]])

# Long version
"""def find_best(X, y, C):
    smallest_error = np.inf     # Start infinity so any real SSE is smaller
    best_index = -1             # Holds the best coefficient set in index

    for idx, coeff in enumerate(C):               # Goes through each coefficient set
        predictions = X.dot(coeff)                # Linear model: X @ coeff -> predicted price
        sse = np.sum((y - predictions) ** 2)      # Sum of squared errors
        if sse < smallest_error:                  # Keeps the best smallest SSE found
            smallest_error = sse
            best_index = idx

    print("the best set is set %d" % best_index)

find_best(X, y, C)"""

# Short simple version
best_index = -1
smallest_error = float('inf')

for i, coeff in enumerate(C):
    sse = np.sum((y - X.dot(coeff)) ** 2)
    if sse < smallest_error:
        smallest_error = sse
        best_index = i

print(f"the best set is set {best_index}")


