setwd('~/Documents/Projects/flpaper/leaf-sparse-kmeans/results/exp82/summary_results/')

# Load libraries
library(ggplot2)
library(ggpubr)
library(lubridate)
library(tidyverse)
library(reshape2)

#
test_accuracies <- read_csv('test_accuracy.csv')

df <- melt(test_accuracies ,  id.vars = 'iter', variable.name = 'Model')

ggplot(df, aes(iter, value)) +
  geom_point(aes(colour = Model)) +
  geom_line(aes(colour = Model)) +
  labs(
    x = "Rounds",
    y = "Accuracy (%)",
    title = "Client-Adaptive K-means",
    subtitle = "Test Accuracy on FEMNIST (lr=0.002, 1000 clients)"
  ) +
  theme_pubclean() +
  theme(legend.position = "bottom")

#
test_losses <- read_csv('test_loss.csv')

df2 <- melt(test_losses ,  id.vars = 'iter', variable.name = 'Model')

ggplot(df2, aes(iter, value)) +
  geom_point(aes(colour = Model)) +
  geom_line(aes(colour = Model)) +
  labs(
    x = "Rounds",
    y = "Loss",
    title = "Client-Adaptive K-means",
    subtitle = "Test Loss on FEMNIST (lr=0.002, 1000 clients)"
  ) +
  theme_pubclean() +
  theme(legend.position = "bottom")

df3 <- data.frame(
  model	= c("baseline", "kmeans_50", "kmeans_55", "kmeans_60", "kmeans_80", "kmeans_85", "kmeans_90", "kmeans_95"),
  test_accuracy = c(0.751315, 0.806338,	0.806338,	0.806338,	0.806338,	0.806338,	0.806338,	0.806338),
  compression_rate = c(1, 2, 1.818181818,	1.666666667,	1.25,	1.176470588,	1.111111111,	1.052631579)
)

ggplot(df3, aes(compression_rate, test_accuracy)) +
  geom_point() +
  geom_line() +
  labs(
    x = "Compression Rate",
    y = "Accuracy (%)",
    title = "Client-Adaptive K-means",
    subtitle = "Test Accuracy on FEMNIST (lr=0.002, 1000 clients)"
  ) +
  theme_pubclean() +
  theme(legend.position = "bottom")
