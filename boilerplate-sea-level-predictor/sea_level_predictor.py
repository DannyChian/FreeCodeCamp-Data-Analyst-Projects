import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')    

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    res1 =linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    print('slope1: ', res1.slope)
    print('y-intercept1: ', res1.intercept)
    predict_2050 = res1.intercept + res1.slope*2050.0
    print('predict_2050：', predict_2050)
    x = np.arange(1880.0, 2051.0, 1)
    y = res1.intercept + res1.slope*x
    print('yyyyyy:',y)
    plt.plot(x, y, 'b', label='first fitted line')
  

  
    # Create second line of best fit
    res2 =linregress(df[df['Year'] >=2000]['Year'], df[df['Year'] >=2000]['CSIRO Adjusted Sea Level'])
    
    print('slope2: ',res2.slope)
    print('y-intercept2: ', res2.intercept)
    predict_2050 = res2.intercept + res2.slope*2050.0
    print('predict_2050：', predict_2050)
    x = np.arange(2000.0, 2051.0, 1)
    y = res2.intercept + res2.slope*x
    plt.plot(x, y, 'y', label='second fitted line')
  
    # Add labels and title
    
    plt.xticks(np.arange(1850.0, 2100.0, step=25.0))
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()