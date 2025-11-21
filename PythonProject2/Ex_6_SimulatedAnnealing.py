import math, random
import numpy as np

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains
def mountains(n):
    h = [0.0] * n
    for _ in range(50):
        c = random.randint(20, n - 20)
        w = random.randint(3, int(math.sqrt(n / 5))) ** 2
        s = random.random()
        left, right = max(0, c - w), min(n, c + w)
        for i in range(left, right):
            h[i] += s * (w -abs(c - i))

    """ Scale the height so that the lowest point is 0.0, the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high - low) for y in h]
    return h"""

    low, high = min(h), max(h)
    rng = high - low
    if rng == 0:                            # guard: flat terrain
        return [0.0] * n
    return [(y - low) / rng for y in h]     # normalize to [0,1]

h = mountains(n)

# start at a random place
x0 = random.randint(1, n - 1)
x = x0

# Keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # Start climbing here
    for step in range(steps):
        # Temperature to be used for simulated annealing
        # Starts large and decreases with each step
        T = 2 * max(0, ((steps - step * 1.2) / steps)) ** 3

        # Randomly move left or right (max. 1000 steps)
        # Use 0 or n-1 to keep falling off the edge
        # S_new is candidate score
        # S_old is current score
        x_new = random.randint(max(0, x - 1000), min(n - 1, x + 1000))

        if h[x_new] > h[x]:
            x = x_new   # If new position is higher, go there
        else:
            # Simulate annealing
            if T > 0:
                accept_prob = math.exp(-(h[x] - h[x_new]) / T)
            else:
                accept_prob = 0 # Avoid division by zero

            # Use "accept_prob" to accept worse move
            if random.random() < accept_prob:
                x = x_new

    return x

x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))

