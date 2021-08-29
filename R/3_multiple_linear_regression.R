dataset <- read.csv('..\\resources\\50_Startups.csv')

# encode state categorical data
dataset$State <- factor(dataset$State,
                        levels = c('New York', 'California', 'Florida'),
                        labels = c(1, 2, 3))

library(caTools)
set.seed(123)
split <- sample.split(dataset$Profit, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# fit the model
# check "new" column names because R modifies names with spaces and & in this case, e.g. R&D Spend to R.D.Spend
# regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = training_set)
# or just . instead of all the independent variables
regressor <- lm(formula = Profit ~ ., data = training_set)
summary(regressor)

y_predicted <- predict(regressor, test_set)
print(y_predicted)

# backward elimination
regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = dataset)
# remove predictor with highest P-value and larger than 0.05 (significance level), here it is State
regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset)
# remove Administration with P-value 0.602 (60.2%), higher than 5% SL
regressor <- lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = dataset)
# now Marketing.Spend has . so it has some statictical significance 0.06 but still above our significance level
regressor <- lm(formula = Profit ~ R.D.Spend, data = dataset)
