library(readxl)
data <- read_excel("data.xlsx", sheet = "data2", 
                   col_types = c("text", "numeric", "numeric", 
                                 "text"))
View(data)

mean(data$Height)
mean(data$Weight)
median(data$Height)

min(data$Height)
max(data$Height)

range(data$Height)

quantile(data$Height, .75)
quantile(data$Height, .25)

sd(data$Height)
var(data$Height)

# iloc replica of pandas
lapply(data[,2:3],mean) # gives mean of column 2 n 3
lapply(data[,2:3],sd)

# to get summary
summary(data)

#anova (tells how two things relate to each other)
# we check if height is varying crop wise







