import numpy
import pandas
from matplotlib import pyplot
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

dataset = pandas.read_csv('../resources/50_Startups.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)

# encode the categorical data
# in transformers, specify the index of the column to apply the hot encoding, e.g. [3]
columnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = columnTransformer.fit_transform(X)
# convert to numpy array
X = numpy.array(X)
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_test)

# train the multiple linear regression model
regression = LinearRegression()
regression.fit(X_train, y_train)
print(f"Coefficients: {regression.coef_.tolist()}")

y_predicted = regression.predict(X_test)
numpy.set_printoptions(precision=2)

# transform horizontal arrays to vertical and concatenate
print(numpy.concatenate((y_predicted.reshape(len(y_predicted), 1), y_test.reshape(len(y_test), 1)), axis=1))

# plot test predictions and model predictions
ten = [list(range(10))]
pyplot.scatter(ten, y_test)
pyplot.scatter(ten, y_predicted, marker=".", color='red')
pyplot.show()

# predict profit based on state
florida_startup_data = [0, 1, 0, 50000, 100000, 10000]
california_startup_data = [1, 0, 0, 50000, 100000, 10000]
new_york_startup_data = [0, 0, 1, 50000, 100000, 10000]
startup_data = [florida_startup_data, california_startup_data, new_york_startup_data]
predicted_profit = regression.predict(startup_data)
print(predicted_profit)
