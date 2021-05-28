import numpy
import matplotlib.pyplot as plt
import pandas

dataset = pandas.read_csv('resources/data.csv')
print(type(dataset))

# split the dataset into -
# x - independent variables, features
# y - dependent variable
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(type(x))
print(x)
print(y)
