rm(list = ls())
setwd("/Users/maxons/Documents/mooc/discrete-optimisation-mooc/week2/data/")

library(dplyr)
library(ggplot2)

data <- read.csv("ks_lecture_dp_2", header = FALSE, sep = " ")
nb_item <- data[1,1]
capacite <- data[1,2]

data <- data[2:(nb_item+1),]
colnames(data) <- c("value", "weight")
row.names(data) <- as.numeric(row.names(data))-1

data$density <- data$value/data$weight

hist(data$value)
hist(data$weight)
hist(data$density)

plot(data$value, data$weight)
