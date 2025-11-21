# Ex. 17 Bag of Words Advance
# Kevin Key
# 11/20/2025

import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 3, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1]]

def find_nearest_pair(data):
    data = np.array(data)

    N = len(data)

    # Create an NxN matrix of distances
    dist = np.empty((N, N), dtype=float)

    # fill the distance matrix
    for i in range(N):
        for j in range(N):
            # Manhattan distance = sum of absolute differences
            dist[i, j] = np.sum(np.abs(data[i] - data[j]))

    # Ignor distances of a row with itself
    np.fill_diagonal(dist, np.inf)

    # Find indices (row numbers) of the smallest distances
    nearest_pair = np.unravel_index(np.argmin(dist), dist.shape)

    # Print the result
    print(nearest_pair)

find_nearest_pair(data)
