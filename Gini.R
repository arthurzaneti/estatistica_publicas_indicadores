# Some packages
if(!require("pacman")) install.packages("pacman")
pacman::p_load(
  "PNADcIBGE",
  "survey",
  "convey",
  "tidyverse",
  "glue",
  "ggplot"
)

# The function that makes the program work
gini1 = function(vec){
  ideal <- seq(0,1, length.out=length(vec))
  return (1- (sum(vec)/sum(ideal)))
}

gini2 = function(vec){
  len <- length(vec)
  bellow_lorenz <- 0
  for (i in 2:len-1){
    trap <- (vec[i] + vec[i+1])/(2*(len-1))
    bellow_lorenz <- bellow_lorenz + trap
  }
  print(bellow_lorenz)
  return (0.5-bellow_lorenz)
}
# Testing the most basic case, other tests might be a good idea
teste <- gini2(c(0,0.2,0.4,0.6,0.8,1))
glue("This should be 0: {teste}")

# Using the function in our data, manually inputted sadly
# All of them stand for Metropolitan Region... (I'm gonna put the region by the side of each line)
RMPA <- gini2(c(0,0.02,0.05,0.09,0.14,0.20,0.27,0.36,0.47,0.64,1)) # Porto Alegre
RMSP <- gini2(c(0,0.01,0.04,0.08,0.13,0.18,0.25,0.33,0.44,0.6,1)) # São Paulo
RMSA <- gini2(c(0,0.01,0.04,0.07,0.11,0.15,0.21,0.29,0.39,0.56,1)) # Salvador 
RMRE <- gini2(c(0,0.01,0.04,0.08,0.12,0.17,0.23,0.31,0.41,0.56,1)) # Recife
RMBH <- gini2(c(0,0.02,0.05,0.08,0.12,0.18,0.24,0.32,0.43,0.6,1)) # Bahia

# Defining a vector to combine into the dataframe
escolaridade <- c("Fundamental completo", "Médio completo", "Superior completo")

# Source here for us to be able to split later when graphing
RMPA_esc_df <-  data.frame(gini2 = c(0.367, 0.385, 0.362), escolaridade, source = "RMPA")
View(RMPA_esc_df)

RMSP_esc_df <- data.frame(gini = c(0.415,0.411,0.417), escolaridade, source= "RMSP")
View(RMSP_esc_df)

# Creating the dataframe with all the information
combined_df <- rbind(RMPA_esc_df, RMSP_esc_df)
View(combined_df)

(bar_chart <- ggplot( combined_df, aes(x=escolaridade, y=gini, fill = source))+ # fill = source is what allows us to differentiate between the regions
  
 geom_bar (stat = "identity", position = "dodge")+ # dodge makes the columns appear side by side
  labs(x = "Escolaridade", y = "Índice de Gini")+ # Labels
  ggtitle("Índice de Gini e escolaridade por região")+ # Title
  scale_fill_manual(values =  c("RMPA" = "#e019bc", "RMSP"= "#13c000"))) # Choosing the colors
