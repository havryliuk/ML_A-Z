import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pandas.read_csv('resources/Salary_Data.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# train the model
regression = LinearRegression()
regression.fit(X_train, y_train)

# save the function y <- x
y_predicted = regression.predict(X_train)

# plot the training set against the function
pyplot.scatter(X_train, y_train, marker='.', color='red')
pyplot.plot(X_train, y_predicted)
pyplot.xlabel('Experience (years)')
pyplot.ylabel('Salary')
pyplot.show()

# compare the real test outcomes against the predicted (function)
# how well our model predicted the outcomes
pyplot.scatter(X_test, y_test, marker='.', color='red')
pyplot.plot(X_train, y_predicted)
pyplot.xlabel('Experience (years)')
pyplot.ylabel('Salary')
pyplot.show()

# use the model to predict salary of employee with 12 years of experience
prediction = regression.predict([[12]])
print(f'employee with 12 years of experience should get {prediction}')

# equation is <code>y = coef_ * x + intercept_</code>
print(f'y = {regression.coef_} * x + {regression.intercept_}')
