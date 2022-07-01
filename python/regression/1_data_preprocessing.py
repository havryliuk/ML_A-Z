import numpy
import pandas
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pandas.read_csv('../../resources/data.csv')
print(type(dataset))

# split the dataset into -
# x - independent variables, features
# y - dependent variable
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(type(X))
print(X)
print(y)

# replace missing values with mean values
simpleImputer = SimpleImputer(missing_values=numpy.nan, strategy='mean')
simpleImputer.fit(X[:, 1:3])
X[:, 1:3] = simpleImputer.transform(X[:, 1:3])
print(X)

# encoding categorical data
columnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = columnTransformer.fit_transform(X)
# convert to numpy array
X = numpy.array(X)
print(X)

labelEncoder = LabelEncoder()
y = labelEncoder.fit_transform(y)
print(y)

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(f'Training set: {X_train}')

# feature scaling
standardScaler = StandardScaler()
X_train[:, 3:] = standardScaler.fit_transform(X_train[:, 3:])
X_test[:, 3:] = standardScaler.transform(X_test[:, 3:])
print(X_train)
print(X_test)
