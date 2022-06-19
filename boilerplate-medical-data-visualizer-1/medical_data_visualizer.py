import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
print(df.head())
# Add 'overweight' column
df['overweight'] = df['weight'] * 10000 / (df['height']**2)
df["overweight"] = df.apply(lambda x: int(bool(x["overweight"] > 25)), axis=1)
# for index,row in df.iterrows():
#     if row['overweight'] > 25:
#        df.at[index,'overweight'] = 1     
#     else:
#         df.at[index,'overweight'] = 0
# df['overweight'] = df['overweight'].astype('int')
# print(df.head())

#Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

def foo_cholesterol(x):
  if x["cholesterol"] == 1:
    return 0
  return 1


def foo_gluc(x):
  if x["gluc"] == 1:
    return 0
  return 1


df["cholesterol"] = df.apply(lambda x: foo_cholesterol(x), axis=1)
df["gluc"] = df.apply(lambda x: foo_gluc(x), axis=1)
print(df.head())
# for index,row in df.iterrows():
#     if row['cholesterol'] ==1 or row['gluc'] == 1:
#        df.at[index,'cholesterol'] = 0    
#        df.at[index,'gluc'] = 0 
#     elif row['cholesterol'] > 1 and row['gluc'] > 1:
#          df.at[index,'cholesterol'] = 1
#          df.at[index,'gluc'] = 1 
# df['cholesterol'] = df['cholesterol'].astype('int')
# df['gluc'] = df['gluc'].astype('int')
#print(df.head())
#print(df['cholesterol'].unique())
#print(np.unique(np.array(df['gluc'])))


# Draw Categorical Plot

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['active','alco','cholesterol','gluc','overweight','smoke','cardio']]
    df_cat_melt = df_cat.melt(id_vars=['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat_count = df_cat_melt.groupby(['variable','value'])['value'].count().reset_index(name="count")
    

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable',hue='value',kind='count',col='cardio',data=df_cat_melt)
    fig.set_axis_labels('variable', 'total')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    
    return fig
#print("hfhfhfhfhffh", fig.axes[0].get_xlabel())

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat_1=df[df['ap_lo'] <= df['ap_hi']]
    df_heat_2=df_heat_1[df_heat_1['height'] >= df_heat_1['height'].quantile(0.025)]
    df_heat_3=df_heat_2[df_heat_2['height'] <= df_heat_2['height'].quantile(0.975)]
    df_heat_4=df_heat_3[df_heat_3['weight'] >= df_heat_3['weight'].quantile(0.025)]
    df_heat = df_heat_4[df_heat_4['height'] <= df_heat_4['height'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.axes_style("white")
    ax = sns.heatmap(corr, mask=mask, annot=True)
    fig = ax.get_figure() 

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
