# Ex.10 Naive Bayes Classifier Advance
# Kevin Key
# 10/21/2025

import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]     # Normal die
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]     # Loaded die (50% chance on side 6)

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # rol the die 10 times; +1 to convert 0-5 to 1-6
    sequence = np.random.choice(6, size=10, p=p) + 1
    for r in sequence:
        print(f"The roll is {r}")
    return sequence

def bayes(sequence):
    odds = 1.0      # Start with prior odds 1:1 (equally likely)
    for r in sequence:
        # Likelihood ratio = P(r|loaded) / P(r|normal)
        # r is in {1..6} so use r-1 to index lists
        lr = p2[r-1] / p1[r-1]
        odds *= lr
    return odds > 1 # True -> loaded more likely, False -> normal more likely

sequence = roll(True)       # Simulator will wet this; True just for a demo run
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")


