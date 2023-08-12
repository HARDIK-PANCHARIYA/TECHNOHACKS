#!/usr/bin/env python
# coding: utf-8

# # TECHNOHACKS

# # Task 1 Perform Data Cleaning

# Clean a dataset by removing missing values and outliers.

# In this task i simply clean the dataset by using verious methods
# 1. Mean/Median, Mode
# 2. bfill,ffill

# # Step 1 Import library

import numpy as np
import pandas as pd
import math as mp

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # Step  2 Read Csv files


df = pd.read_csv('train.csv')


df.info()

df.head()

df.tail()

# # It will return the count of null values in each column

df.isnull().sum()

#as we observe that
#Age have total 177 null values
#Cabinn have total 687 null values
#Embarked have total 2 null values

df.dtypes

# # using mean we fill the Age null values

mean=round(df["Age"].mean(),2)
mean

df["Age"].fillna(mean,inplace=True)
df

df.isnull().sum()

# # using mode we fill the Enbarked null values

m=df["Embarked"].mode()
m

m=df["Embarked"].mode()[0]
m

df["Embarked"].fillna(m,inplace=True)
df

df.isnull().sum()

# # using bfill and ffill we fill the Cabin null values

df.bfill(limit=490,inplace=True)
df

df.isnull().sum()

df.ffill(inplace=True)
df

df.isnull().sum()

# # Finally all the data set null values are get clear

df

df.dtypes

# # as we observed that Age and Fare data type is float 64 
#Age can be never in the float type so we can convert it into the int type
#and also we can convert the Fare into int type to get more clear dataset
#So we can now change the datatype 

df = df.astype({"Age": int, "Fare": int})

df.dtypes

# # data type of Age and Fear converted into int

df

df.to_csv('cleandatatask1.csv', index=False)

