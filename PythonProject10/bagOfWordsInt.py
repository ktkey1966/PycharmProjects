# Ex. 17 - Bag of Words Intermediate
# Kevin Key
# 11/20/2025


# This is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # Calculate the sum of absolute differences between two rows
    total =0
    for i in range(len(row1)):
        total += abs(row1[i] - row2[i])
    return total

def all_pairs(data):
    # Calculate distances for all pairs of rows
    dist = []
    for i in range(len(data)):
        row_distances = []
        for j in range(len(data)):
            row_distances.append(distance(data[i], data[j]))
        dist.append(row_distances)
    print(dist)


all_pairs(data)


