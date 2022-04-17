install.packages("ggplot2")
library(ggplot2)
library(readxl)

library(readxl)
x <- read_excel("ggdata.xlsx", sheet = "gg1", 
                     col_types = c("text", "numeric", "text", 
                                   "text"))
View(x)

# simple gg plot
ggplot(data=x,mapping = aes(x=crop, y=height))+
  geom_point()

# smart gg plot (scatter)
ggplot(x,aes(crop,height))+
  geom_point(size=4)+
  geom_line(size=3)

# smart gg plot (boxplot)
ggplot(x,aes(crop,height))+geom_boxplot(col="blue")+
  geom_line()+
  geom_point(col="purple")





