import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col=['date'])
print(df.head(10))
# Clean data
df = df.sort_values(by=['value'])
df_clean = df.loc[lambda df: (df['value'] > df['value'].quantile(0.025))&(df['value'] < df['value'].quantile(0.975)) ]
df_clean = df_clean.sort_index()
print(df_clean.head(10))

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_clean.index, df_clean['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
 
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.copy()
    df_bar.reset_index(inplace=True)
    df_bar = df_bar.groupby([df_bar['date'].dt.year, df_bar['date'].dt.strftime('%B')],sort=False)['value'].mean().rename_axis(['year','month'])
    df_bar = df_bar.to_frame()
    df_bar.reset_index(inplace=True)
    
    # Draw bar plot
    fig, ax = plt.subplots()
    ax = sns.barplot(x='year', y='value', hue='month', data=df_bar, hue_order=['January','February','March','April','May','June','July','August','September','October','November','December'])
    fig = ax.get_figure()
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')   
    ax.legend(title='Months', loc='upper left', prop={'size': 8})
 

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # fig, axes = plt.subplots(1, 2,figsize=(20,8))
    # sns.boxplot(ax=axes[0], x='year', y='value', data=df_box)
    # sns.boxplot(ax=axes[1], x='month', y='value', data=df_box, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    # axes[0].set(xlabel='Year', title='Year-wise Box Plot (Trend)')
    # axes[1].set(xlabel='Month', title='Month-wise Box Plot (Seasonality)')
    # axes.set_ylable('Page Views')

    fig, (ax1,ax2) = plt.subplots(1, 2,figsize=(20,8))
    sns.boxplot(ax=ax1, x='year', y='value', data=df_box)
    sns.boxplot(ax=ax2, x='month', y='value', data=df_box, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    ax2.set(xlabel='Month',ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
