# MoviesAnalysis

Movie Images
This script generates visualizations of movie data, analyzing the data in terms of genre, revenue, and year. The script uses the following libraries:

pandas
numpy
matplotlib
statsmodels

Plot 1
The first plot displays the gross revenue for the top 20 comedy films since 1980. The data is read from a CSV file named 'movies.csv' and filtered to include only comedy films. The top 20 films are then selected and a bar plot is created, with the gross revenue on the y-axis and the film title on the x-axis. The resulting plot shows the gross revenue in billions of dollars for each of the top 20 comedy films.

Plot 2
The second plot shows the gross revenue over time for the top 500 comedy films since 1980. The data is read from the same CSV file as in Plot 1 and filtered to include only comedy films. The top 500 films are then selected and a scatter plot is created, with the gross revenue on the y-axis and the year on the x-axis. A regression line is also included to show the trend in gross revenue over time.

Plot 3
The third plot displays the average gross revenue for films in each genre since 1980. The data is read from the same CSV file as in Plots 1 and 2 and grouped by genre. The average gross revenue for each genre is then calculated, and a bar plot is created with the genre on the x-axis and the average gross revenue on the y-axis.

How to Use
To use this script, you can run the script using a Python interpreter or from the command line. The resulting plots will be displayed in separate windows.

Requirements
This script requires the following libraries:

pandas
numpy
matplotlib
statsmodels
These can be installed using pip by running the following command:

pip install pandas numpy matplotlib statsmodels
