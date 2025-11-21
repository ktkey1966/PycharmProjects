import numpy as np
import random

N = 100
steps = 3000
tracks = 50

# landscape (note the 0.07 coefficients)
def generator(x, y, x0=0.0, y0=0.0):
    return (np.sin((x/N - x0)*np.pi) +
            np.sin((y/N - y0)*np.pi) +
            0.07*np.cos(12*(x/N - x0)*np.pi) +
            0.07*np.cos(12*(y/N - y0)*np.pi))

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x, y
    for step in range(steps):
        # cooling per the hint
        T = max(0.0, ((steps - step) / steps)**3 - 0.005)

        for i in range(tracks):
            xi, yi = x[i], y[i]
            x_new = np.random.randint(max(0, xi - 2), min(N, xi + 3))
            y_new = np.random.randint(max(0, yi - 2), min(N, yi + 3))

            s_old = h[xi, yi]
            s_new = h[x_new, y_new]

            if s_new >= s_old:
                x[i], y[i] = x_new, y_new
            else:
                if T > 0.0:
                    prob = np.exp(-(s_old - s_new) / T)
                    if random.random() < prob:
                        x[i], y[i] = x_new, y_new

    hits = sum((x[j] == peak_x) and (y[j] == peak_y) for j in range(tracks))
    print(hits)   # grader expects just the integer

main()




