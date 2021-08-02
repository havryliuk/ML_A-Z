# Title     : Simple linear regression
# Created by: Oleksandr_Gavryliuk
# Created on: 13-Jul-21

dataset <- read.csv('..\\resources\\Salary_Data.csv')

library(caTools)
set.seed(123)
split <- sample.split(dataset$Salary, SplitRatio = 2/3)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)
print(training_set)
print(test_set)

# fit the linear model
regressor <- lm(formula = Salary ~ YearsExperience, data = training_set)
summary(regressor)

# predict salaries for the test set
y_predicted <- predict(regressor, test_set)

# predict salary for employee with 12 years of experience
twelve_years_salary <- predict(regressor, data.frame("YearsExperience" = 12))

# plot
library(ggplot2)
ggplot() +
  geom_point(aes(training_set$YearsExperience, training_set$Salary),
             colour = 'red') +
  geom_line(aes(training_set$YearsExperience, predict(regressor, training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Experience (years') +
  ylab('Salary (US dollars')

ggplot() +
  geom_point(aes(test_set$YearsExperience, test_set$Salary),
             colour = 'red') +
  geom_line(aes(training_set$YearsExperience, predict(regressor, training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (test set)') +
  xlab('Experience (years)') +
  ylab('Salary (US dollars)')