import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pandas.read_csv('../resources/Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# build linear model
linear_regression = LinearRegression()
linear_regression.fit(X, y)
y_predicted = linear_regression.predict(X)

# transform matrix of features to the matrix of powered features
polynomial_features_2 = PolynomialFeatures(degree=2)
X_powered_2 = polynomial_features_2.fit_transform(X)

# build polynomial regression model
polynomial_regression_2 = LinearRegression()
polynomial_regression_2.fit(X_powered_2, y)
y_power_2_predicted = polynomial_regression_2.predict(X_powered_2)

# calculate predicted salary with linear and polynomial models
years = 7.5
salary_level_7_5_linear = linear_regression.predict([[years]])
salary_level_7_5_poly = polynomial_regression_2.predict(polynomial_features_2.fit_transform([[years]]))
print(f'Predicted salary for 7.5 years (linear): {salary_level_7_5_linear}')
print(f'Predicted salary for 7.5 years (polynomial): {salary_level_7_5_poly}')

pyplot.scatter(X, y)
pyplot.plot(X, y_predicted)
pyplot.plot(X, y_power_2_predicted)
pyplot.scatter(years, salary_level_7_5_linear, marker='x', color='red')
pyplot.scatter(years, salary_level_7_5_poly, marker='x', color='red')
pyplot.annotate(round(salary_level_7_5_linear[0]), (years, salary_level_7_5_linear))
pyplot.annotate(round(salary_level_7_5_poly[0]), (years, salary_level_7_5_poly))
pyplot.show()
