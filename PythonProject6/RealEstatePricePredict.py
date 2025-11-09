# Ex. 11 - Real Estate Price Prediction
# Kevin Key
# 10/28/2025

# input values for one mokkis: size, size of sauna, distance to water, number of indoor bathrooms,
# proximity of neighbours

x = [155, 15, 5, 1, 200]
c = [3000, 200, -50, 5000, 100]     # coefficient values

prediction = c[0] *x[0] + c[1] *x[1] + c[2] *x[2] + c[3] *x[3] + c[4] *x[4]

print(prediction)

