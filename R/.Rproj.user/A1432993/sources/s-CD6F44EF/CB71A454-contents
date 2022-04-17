library(readxl)

my_data <- read_excel("data.xlsx", sheet = "data", 
                      col_types = c("text", "numeric", "numeric"))
View(my_data)
# to view structure of data
str(my_data)
# to view data top 5
head(my_data)

# simple plot 
plot(my_data)
# boxplot(same data types)
boxplot(my_data$Height, my_data$Weight)
boxplot(my_data$Crop, my_data$Height)

#boxplot( different data types)
boxplot(my_data$Height ~ my_data$Crop)
