# Ex. 15 Vector Distance
# Kevin Key
# 11/13/2025

import numpy as np

# Option A
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


# Option B
'''def dist(a, b):
    sum_a = 0
    sum_b = 0
    for ai in a:
        sum_a = sum_a + ai
    for bi in b:
        sum_b = sum_b + bi
    return np.sqrt((sum_a - sum_b)**2)'''


""" Correct answer is Option A: it computes the Euclidean distance."""

