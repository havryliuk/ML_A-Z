# Title     : Data Preprocessing
# Created by: Oleksandr_Gavryliuk
# Created on: 28-May-21

# import the dataset
dataset <- read.csv('resources\\data.csv')
print(dataset)

# handle missing data
dataset$Age <- ifelse(is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      dataset$Age)
dataset$Salary <- ifelse(is.na(dataset$Salary),
                         ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                         dataset$Salary)
print(dataset)

# encode categorical data
dataset$Country <- factor(dataset$Country,
                          # specify names for factors (columns) in the vector c
                          levels = c('France', 'Spain', 'Germany'),
                          labels = c(1, 2, 3))
dataset$Purchased <- factor(dataset$Purchased,
                          # specify names for factors (columns) in the vector c
                          levels = c('No', 'Yes'),
                          labels = c(0, 1))
print(dataset)

# split dataset into training and test datasets
# install.packages('caTools')
library(caTools)
# random number for randomly selecting test and train data, can be any number
set.seed(123)
# defines which rows will be selected: TRUE - training set, FALSE - test set
split <- sample.split(dataset$Purchased, 0.8)
print(split)

training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)
print(training_set)
print(test_set)

# feature scaling
training_set[, 2:3] <- scale(training_set[, 2:3])
test_set[, 2:3] <- scale(test_set[, 2:3])
