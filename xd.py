import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# meed to reshape because x needs to be a 2d array, one column, many rows
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

print(x)
print(y)

plt.plot(x, y, 'o', color='purple')
plt.ylabel("Y axis title (Price)")
plt.xlabel("X axis title (Quantity)")

model = LinearRegression().fit(x, y)

# r^2 range between 0 and 1, indicates the level correlation
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

# prediction for y when x is 0 (y axis interception), returns a scalar
print('intercept:', model.intercept_)

# slope of the line of regression, returns an array
print('slope:', model.coef_)
slope = (model.coef_).item()

# same as y_pred = model.intercept_ + model.coef_ * x
# the y predictions based on the calculated curve for the x values
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

plt.plot(x, slope*x + model.intercept_, color='red')
plt.show()