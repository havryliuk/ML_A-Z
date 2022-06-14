import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset = pandas.read_csv('../../resources/Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# transform salaries into a two-dimensional array from row into column
y = (y.reshape(len(y), 1))
print(y)

# feature scaling
standard_scaler_X = StandardScaler()
X = standard_scaler_X.fit_transform(X)
print(X)

standard_scaler_y = StandardScaler()
y = standard_scaler_y.fit_transform(y)
print(y)

# train the SVR model (support
svr = SVR(kernel='rbf')
svr.fit(X, y)

level_6_5_scaled = standard_scaler_X.transform([[6.5]])
print(level_6_5_scaled)
predicted_salary = svr.predict(level_6_5_scaled)
print(predicted_salary)
print(standard_scaler_y.transform([predicted_salary]))
