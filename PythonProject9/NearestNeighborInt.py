# Ex 16 Nearest Neighbor Intermediate
# Kevin Key
# 11/13/2025

"""
The program below uses the library sklearn to generate a random dataset. You don't need to be familiar with sklearn, we explain all the necessary information below.
Each sample in the dataset has two input features X and one binary output class y.
We can think of a sample as a cabin, with its size and price as its input features, and whether we like it (1) or not (0) as its output class.

The program's goal is to classify the cabins based on their nearest neighbor's class.
That is, predict whether we would like a cabin based on our opinion of another cabin with the most similar input features.

The program first generates the random dataset and splits it into training and test sets.
Then, for each cabin in the test set, it identifies its nearest neighbor from the cabins in the train set using the distance function.
However, the program has very high standards and dislikes all the cabins y_predict[i] = 0.

Your goal is to make the program smarter by predicting the output class (y_predict)
for each cabin in the test set based on the output class (y_train) of its nearest neighbor.
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
    total = 0
    for ai, bi in zip(a, b):
        total = total + (ai - bi) ** 2
    return np.sqrt(total)

def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines

    # Process each of the test data points
    for i, test_item in enumerate(X_test):
        # Calculate distances from test item to all training items
        distances = [dist(train_item, test_item) for train_item in X_train]

        # Find the index of the nearest neighbor
        nearest = np.argmin(distances)

        # Create a line connecting the test item and its nearest neighbor
        lines.append(np.stack((test_item, X_train[nearest])))

        # Predict the output class of the test item based on its nearest neighbor
        y_predict[i] = y_train[nearest]

    print(y_predict)

if __name__ == "__main__":
    main(X_train, X_test, y_train, y_test)


