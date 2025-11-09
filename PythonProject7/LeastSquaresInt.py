# Ex. 12 Least Squares Intermediate
# Kevin Key
# 10/29/2025

import numpy as np

X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])

y = np.array([250000, 60000, 525000])
c = np.array([3000, 200, -50, 5000, 100])       # Coefficients values

# Long version
"""def squared_error(x, y, coeffs):
    sse = 0.0
    for xi, yi in zip(x, y):
        # predicted price for this cabin (dot product of features and coefficients)
        prediction = np.dot(xi, coeffs)
        # Add squared difference to the running total
        sse += (yi - prediction) ** 2
    print(f"Sum of Squared Errors (SSE): {sse:.2f}")
    return sse

# Run function
squared_error(X, y, c)"""

# One-line vectorized version
predictions = X.dot(c)
sse = np.sum((y - predictions) ** 2)

print("Sum of Squared Errors (SSE):", sse)


