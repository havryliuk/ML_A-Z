dataset <- read.csv('C:\\Users\\Oleksandr_Gavryliuk\\IdeaProjects\\ML_A-Z\\resources\\Position_Salaries.csv')
dataset <- dataset[2:3]

# we won't split the dataset into training and test because the dataset is very small
#
# library(caTools)
# set.seed(123)
# split <- sample.split(dataset$Salary, SplitRatio = 0.8)
# training_set <- subset(dataset, split == TRUE)
# test_set <- subset(dataset, split == FALSE)

# train linear model
linear_regressor <- lm(formula = Salary ~ Level, data = dataset)
summary(linear_regressor)

linear_predicted <- predict(linear_regressor, dataset)

# add two more columns with the values of Salary powered
dataset$Level2 <- dataset$Level^2
dataset$Level3 <- dataset$Level^3
# dataset$Level4 <- dataset$Level^4
# build model based on all columns except Salary; '.' means 'all other columns'
polynomial_regressor <- lm(formula = Salary ~ ., data = dataset)

polynomial_predicted <- predict(polynomial_regressor, dataset)
level <- 6.5
seven_and_half_level_salary_linear <- predict(linear_regressor, data.frame("Level" = level))
seven_and_half_level_salary_poly <- predict(polynomial_regressor, data.frame("Level" = level, "Level2" = level^2, "Level3" = level^3))

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = linear_predicted),
            colour = 'blue') +
  geom_line(aes(x = dataset$Level, y = polynomial_predicted),
            colour = 'green') +
  geom_point(aes(x = level, y = seven_and_half_level_salary_linear)) +
  geom_text(aes(
    x = level,
    y = seven_and_half_level_salary_linear,
    label = round(seven_and_half_level_salary_linear)),
            nudge_x = 0.5, nudge_y = 0.5) +
  geom_point(aes(x = level, y = seven_and_half_level_salary_poly)) +
  geom_text(aes(x = level, y = seven_and_half_level_salary_poly, label = round(seven_and_half_level_salary_poly)),
            nudge_x = 0.5, nudge_y = 0.5) +
  ggtitle('Truth or Bluff (linear)') +
  xlab('Level') +
  ylab('Salary')
