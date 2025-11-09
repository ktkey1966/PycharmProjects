import numpy as np

def generate(p1):
    # Generate 10,000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], size=10000, p=[1-p1, p1])
    return seq

def count(seq):
    # Count the number of occurrences of 11111 in the sequence
    count_11111 = 0
    for i in range(len(seq) - 4):
        if np.all(seq[i:i+5] == 1):
            count_11111 += 1
    return count_11111

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))


