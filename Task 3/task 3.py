# # Task 3 : Visualization using Histogram

# - Create a histogram or bar chart to visualize the distribution of data in a dataset

# In this task i simply plot the 
# 
# 1. Histograms
# 2. barplot
# 3. distplot
# 4. facetgrid bar

# # Step 1 Import library

# import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # Step 2 Read Csv files

df = pd.read_csv('iris.csv')


# # Step 3 Getting information about the Dataset 

df.info()

df

df['species'].unique()

df.groupby('species').count()


# # Histograms

fig, axes = plt.subplots(2, 2, figsize=(15,12))
axes[0,0].set_title("Distribution of Sepal Width")
axes[0,0].hist(df['sepal_width'], bins=5);
axes[0,1].set_title("Distribution of Sepal Length")
axes[0,1].hist(df['sepal_length'], bins=7);
axes[1,0].set_title("Distribution of Petal Width")
axes[1,0].hist(df['petal_width'], bins=6);
axes[1,1].set_title("Distribution of Petal Length")
axes[1,1].hist(df['petal_length'], bins=6);


# observation
# 
# 1 . higest frequency of sepal width is between 3.0 to 3.5 and lower frequency is between 4.0 to 4.4
# 
# 2 . higest frequency of sepal length is between 5.5 to 6.0 and lower frequency between 7.5 to 7.4
# 
# 3 . higest frequency of petal width is between 1.0 to 0.6 and lower frequency is between 0.6 to 1.1
# 
# 4 . higest frequency of spetal length is between 1 to 2 and lower frequency is between 3 to 4

# # barplot

fig, axes = plt.subplots(2, 2, figsize=(16,13))
sns.barplot(y='sepal_length',x='species',data=df,ax=axes[0,0])
sns.barplot(y='sepal_width',x='species',data=df,ax=axes[0,1])
sns.barplot(y='petal_length',x='species',data=df,ax=axes[1,0])
sns.barplot(y='petal_width',x='species',data=df,ax=axes[1,1])


# observation
# 
# setosa length is always smaller size species in all the comparision expect in sepal width it have largest sepal weidth among all species
# 
# versiclor is always mediam size species in all the compariseion
# 
# viginica is largest size species in all the comparision

cols = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length']
plt.figure(figsize=(20,4), dpi=100)
i = 1
for col in cols:
    plt.subplot(1,11,i)
    sns.distplot(df[col])
    i = i+1
plt.tight_layout()
plt.show()


# observation
# 
# show the average distribution with respect to density in each columns

sns.FacetGrid(data=df,hue="species",height=9).map(sns.distplot,"petal_width")
plt.legend(bbox_to_anchor=(1,1))

sns.FacetGrid(data=df,hue="species",height=9).map(sns.distplot,"petal_length")
plt.legend(bbox_to_anchor=(1,1))

sns.FacetGrid(data=df,hue="species",height=9).map(sns.distplot,"sepal_width")
plt.legend(bbox_to_anchor=(1,1))

sns.FacetGrid(data=df,hue="species",height=9).map(sns.distplot,"sepal_length")
plt.legend(bbox_to_anchor=(1,1))


# observation in above 4 graphs
# 
# sepal length and sepal width are overlaping that mes their size are same
# 
# petal length and petal width setosaa is get seprated clearly
