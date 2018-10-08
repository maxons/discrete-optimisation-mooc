rm(list = ls())
setwd("/Users/maxons/Documents/mooc/discrete-optimisation-mooc/week2/data/")

library(dplyr)
library(ggplot2)

# list.files()

explore_data <- function(file_name)
{
  data <- read.csv(file_name, header = FALSE, sep = " ")
  
  nb_item <- data[1,1]
  capacite <- data[1,2]
  
  data <- data[2:(nb_item+1),]
  colnames(data) <- c("value", "weight")
  row.names(data) <- as.numeric(row.names(data))-1
  
  data$density <- data$value/data$weight
  
  par(mfrow=c(2,2))
  hist(data$value)
  hist(data$weight)
  hist(data$density)
  
  
  plot(data$value, data$weight, title(main=file_name))
}

n = length(list.files())

for (ii in 1:n)
  explore_data(list.files()[ii])

