import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',', float_precision='legacy')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(13,8))
    df.plot(kind='scatter',
                   x='Year',
                   y='CSIRO Adjusted Sea Level')

    # Create first line of best fit

    #use lingress function to find the slope, intercept, r_value, p_value, std_err
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #use numpy array to extend the years of regression line, predicting past original dataset through 2050
    years = np.arange(1880, 2051, 1)

    #set up the intercept slope to extended years, based on original data.
    regr = [line.intercept + line.slope * x for x in years]

    plt.xticks(range(1850, 2076,25))

    plt.plot(years, regr, 'r')

    # Create second line of best fit

    #regresson analysis from 2000 to most recent year in data(2013)
    line2 = linregress(df[df['Year'] >= 2000]['Year'],
                       df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    #set up np array for 2000 to 2050
    years2 = np.arange(2000, 2051, 1)

    #set up regression line for 2000 to 2050
    regr2 = [line2.intercept + line2.slope * x for x in years2]

    plt.plot(years2, regr2, 'r')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
