# Ex 16 Nearest Neighbor Advance
# Kevin Key
# 11/13/2025

"""
In the basic nearest neighbor classifier, the only thing that matters is the class label of the nearest neighbor.
But the nearest neighbor may sometimes be noisy or otherwise misleading.
Therefore, it may be better to also consider the other nearby data points in addition to the nearest neighbor.

This idea leads us to the so called k-nearest neighbor method, where we consider all the k nearest neighbors.
If k=3, for example, we'd take the three nearest points and choose the class label based on the majority class among them.

The program below uses the library sklearn to generate a random dataset.
You don't need to be familiar with sklearn, we explain all the necessary information below.
Each sample in the dataset has two input features (X) and one binary output class (y).
We can think of a sample as a cabin, with its size and price as its input features, and whether we like it (1) or not (0) as its output class.

The program first generates the random dataset and splits it into training and test sets.
Then, for each cabin in the test set, it identifies its nearest neighbor (k=1) from the cabins in the train set using the distance function.
However, the program has very high standards and dislikes all the cabins y_predict[i] = 0.

Your goal is to make the program smarter by predicting the output class (y_predict) for each cabin in the test set based on the majority output class (y_train) of its three nearest neighbor (k=3).
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Generate random dataset
X, y = make_blobs(n_samples=16, centers=2, n_features=2, center_box=(-2, 2))

# Scale data between 0 and 1
X = MinMaxScaler().fit_transform(X)

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

# Placeholder for predicted output classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# Produce line segments that connect the test data points
# with their nearest neighbor in the training data
lines = []

# Distance function
def dist(a, b):
    sum_sq = 0
    for ai, bi in zip(a, b):
        sum_sq = sum_sq + (ai - bi) ** 2
    return np.sqrt(sum_sq)

def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines

    k = 3 # Classify based on 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # Calculate distances to all training data points
        distances = [dist(test_item, train_item) for train_item in X_train]

        # Find the k nearest neighbors
        nearest_k_indices = np.argsort(distances)[:k]

        # Create line segments to all k neighbors
        for idx in nearest_k_indices:
            lines.append(np.stack((test_item, X_train[idx])))

        # Get the classes of the k nearest neighbors
        neighbor_classes = y_train[nearest_k_indices]

        # Classify based on majority class
        counts = np.bincount(neighbor_classes)  # Index 0 = count of class 0, index 1 = count of class 1, etc.
        y_predict[i] = np.argmax(counts)        # class with highest count

    print(y_predict)

if __name__ == "__main__":
    main(X_train, X_test, y_train, y_test)

