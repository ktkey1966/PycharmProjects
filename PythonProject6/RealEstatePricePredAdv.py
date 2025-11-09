# Ex. 11: Real Estate Price Prediction
# Kevin Key
# 10/28/2025

# input values for three mokkis: size, size of sauna, distance to water,
# number of indoor bathrooms, proximity of neighbors

X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200, -50, 5000, 100]

def predict(X, c):
    # loop through each cabin (row in X)
    for features in X:
        # dot product of coefficients and this cabin's features
        price = 0
        for coef, val in zip(c, features):
            price += coef * val
        print(price)

predict(X, c)







