from sklearn import linear_model
import numpy as np 

x = np.array([1, 2, 3, 5, 6]).reshape((-1, 1))
y = np.array([1, 4, 6, 27, 38])

model = linear_model.LinearRegression()
model.fit(x, y)

print(model.coef_, model.intercept_)