import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from matplotlib import pyplot

dataset = pandas.read_csv('../../resources/Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# transform salaries into a two-dimensional array from row into column
print('Before transformation: {y}'.format(y=y))
y = (y.reshape(len(y), 1))
print('After transformation: {y}'.format(y=y))

# feature scaling
standard_scaler_X = StandardScaler()
X = standard_scaler_X.fit_transform(X)
print('Features scaled: {x}'.format(x=X))

standard_scaler_y = StandardScaler()
y = standard_scaler_y.fit_transform(y)
print('Dependent variable scaled: {y}'.format(y=y))

# train the SVR model (support vector regression)
svr = SVR(kernel='rbf')
svr.fit(X, y)

level_6_5_scaled = standard_scaler_X.transform([[6.5]])
print('Input level 6.5 years scaled: {level}'.format(level=level_6_5_scaled))
predicted_salary = svr.predict(level_6_5_scaled)
print('Predicted salary: {salary}'.format(salary=predicted_salary))
# reverse scaling
print('Predicted salary (inverse scaled): {salary}'
      .format(salary=standard_scaler_y.inverse_transform([predicted_salary])))

# visualize the SVR model
X_inverse_transformed = standard_scaler_X.inverse_transform(X)
y_predicted = svr.predict(X)
pyplot.title('SVR')
pyplot.scatter(X_inverse_transformed, standard_scaler_y.inverse_transform(y), color='red')
pyplot.plot(X_inverse_transformed, standard_scaler_y.inverse_transform([y_predicted]).flatten(), color='blue')
pyplot.show()
