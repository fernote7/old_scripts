setwd("C:/Users/fernando.ormonde/Dropbox/Fernando/Python/Kaggle/RStudio") #set the directory
train <- read.csv("C:/Users/fernando.ormonde/Dropbox/Fernando/Python/Kaggle/train.csv") #open file
View(train)
str(train) #structure of the data frame
train <- read.csv("train.csv", stringsAsFactors=FALSE) # if you want to import and manipulate the strings on your data
table(train$Survived) #column of the train.csv isolated and put in a table
a = table
prop.table(a(train$Survived)) #proportion of passengers dead and alive
test$Survived = rep(0, 418) #after opening test file and reading, create column or replace existent with the repetion of zeros, 418 times.
summary(train$Sex) #sum??rio
prop.table(a(train$Sex, train$Survived)) #propor????o de sobreviventes de cada g??nero no total de passageiros
prop.table(a(train$Sex, train$Survived),1) #propor????o de sobreviventes de cada g??nero \ se usar '2' ter??amos a propor????o das colunas
test$Survived <- 0 # changes all the column to zeros
test$Survived[test$Sex == 'female'] <- 1 #change the subset of female to '1'
submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived) #creates submit with ID and Survived as headers
write.csv(submit, file = "theyallperish2.csv", row.names = FALSE) #creates a csv file with the information
train$Child <- 0 #creates column Child
train$Child[train$Age < 18] <- 1 #overwrites column for all those who are less than 18 (imput 1)
aggregate(Survived ~ Child + Sex, data=train, FUN = sum)
aggregate(Survived ~ Child + Sex, data=train, FUN = length)
aggregate(Survived ~ Child + Sex, data=train, FUN=function(x) {sum(x)/length(x)}) #aggregate data
train$Fare2 <- '30+'
train$Fare2[train$Fare < 30 & train$Fare >= 20] <- '20-30'
train$Fare2[train$Fare < 20 & train$Fare >= 10] <- '10-20'
train$Fare2[train$Fare < 10] <- '<10'
aggregate(Survived ~ Fare2 + Pclass + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

> test$Survived <- 0
> test$Survived[test$Sex == 'female'] <- 1
> test$Survived[test$Sex == 'female' & test$Pclass == 3 & test$Fare >= 20] <- 0

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train, method="class") #rpart does something similar to aggregate, method class, opposed to 'anova', used because we do not want to predict a continuous variable
plot(fit)
text(fit)

install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

Prediction <- predict(fit, test, type = "class")
submit <- data.frame(PassengerId = test$PassengerId, Survived = Prediction)
write.csv(submit, file = "myfirstdtree.csv", row.names = FALSE)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train, method="class", control=rpart.control(minsplit=2, cp=0))
fancyRpartPlot(fit)
