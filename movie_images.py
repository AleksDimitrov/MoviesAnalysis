# File: movie_images.py
# Author: Aleksander Dimitrov
# Description: This script generates images that represent visualizations of movie data, analyzing the data
#              in terms of genre, revenue, and year

# import libraries for dealing with data
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.pyplot import figure, tick_params
import statsmodels.api as sm
import json

################ Start of Plot 1 ################
df1 = pd.read_csv("movies.csv") # read in CSV
plt.figure(facecolor="#B29700") # make outer area dark gold
ax = plt.axes(facecolor="#BEC2CB") # make inner area light silver
comedy = df1.loc[df1.genre == "Comedy"].sort_values(by="gross", ascending=False) # gets rows with Comedy genre sorted by gross revenue in descending order
comedy = comedy[:20] # gets the first 20 rows from the comedy DF
graph1 = pd.Series(comedy.gross.values, comedy.name.values) # makes a series using the gross revenue as data and names as index
graph1.dropna() # drop NA values
graph1.plot.bar(rot=90, figsize=(12, 9), color="green") # make bar plot
plt.title("Gross Revenue for Top 20 \nComedy Films Since 1980", size=25, color="white") # setup title
plt.ylabel("Gross Revenue ($Billions)", size=18, color="white") # setup main y-axis label
plt.xlabel("Film Title", size=18, color="white") # setup main x-axis label
plt.ylim(top=1000000000) # vertical limit = $1 billion
plt.subplots_adjust(bottom=0.47) # shift bottom of graph up to fit in window
tick_params(labelsize=15, colors="white") # setup x-axis and y-axis interval labels
plt.show() # show the resulting plot
################ End of Plot 1 ################

################ Start of Plot 2 ################
df2 = pd.read_csv("movies.csv") # read in CSV
plt.figure(figsize=(12, 9), facecolor="#B29700") # make outer area dark gold
plt.axes(facecolor="#BEC2CB") # make inner area light silver
comedy2 = df2.loc[df2.genre == "Comedy"].sort_values(by="gross", ascending=False) # gets rows with Comedy genre sorted by gross revenue in descending order
df2.dropna() # drop NA values
comedy2 = comedy2[:500] # gets the first 500 rows from the comedy2 DF
graph2 = pd.Series(comedy2.gross.values, comedy2.year.values) # makes a series using the gross revenue as data and names as index
graph2.dropna() # drop NA values
ax = graph2.plot(linestyle='', marker='o', markersize=5, alpha=0.75, color="green") # make scatter plot
x = graph2.index.values # gets the values from the index
X = sm.add_constant(x) # adds each constant from the index
model = sm.OLS(graph2, X) # Ordinary Least Squares
line = model.fit() # trains the model
line.summary() # interprets the regression
y = line.params['x1'] * x + line.params['const'] # setup y=mx+b equation
plt.plot(x, y, linewidth=4, color="red") # graph the regression line
plt.xlabel("Time (Years)", fontsize=18, color="white") # setup main x-axis label
plt.ylabel("Gross Revenue ($100Millions)", fontsize=18, color="white") # setup main y-axis label
plt.title("Gross Revenue over Time for Top 500 \nComedy Films Since 1980", fontsize=24, color="white") # setup title
tick_params(labelsize=15, colors="white") # setup x-axis and y-axis interval labels
plt.show() # show the resulting plot
################ End of Plot 2 ################

################ Start of Plot 3 ################
df3 = pd.read_csv("movies.csv") # read in CSV
fig = plt.figure(facecolor="#B29700") # make outer area dark gold
ax = plt.axes(facecolor="#BEC2CB") # make inner area light silver
newData = df3.groupby('genre').gross.mean() # for getting avg gross revenues for each genre
newData.dropna() # drop NA values
newData.plot.bar(x=2, y=12, color="green") # make bar plot
plt.title("Average Gross Revenue of \nFilms vs Genre Since 1980",size=30, color="white") # setup title
plt.xlabel("Genre",size=20, color="white") # setup main x-axis label
plt.ylabel("Average Gross Revenue ($100Millions)",size=20, color="white") # setup main y-axis label
plt.subplots_adjust(bottom=0.2) # shift bottom of graph up to fit in window
tick_params(labelsize=15, color="white", colors="white") # setup x-axis and y-axis interval labels
plt.xticks(rotation=90) # rotate x-axis interval labels 90 degrees
plt.show() # show the resulting plot
################ End of Plot 3 ################