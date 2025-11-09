# Ex. 11: Real Estate Price Prediction
# Kevin Key
# 10/28/2025


# input values for three mokkis:
# - size [m^2],
# - size of sauna [m^2],
# - distance to water [m],
# - number of indoor bathrooms,
# - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200, -50, 5000, 100]

def predict(X, c):
    for x in X:     # loop through each cabin
        price = 0
        for i in range(len(c)):     # multiply each coefficient by its corresponding value
            price += c[i] * x[i]
        print(price)

predict(X, c)
