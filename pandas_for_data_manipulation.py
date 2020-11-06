# -*- coding: utf-8 -*-
"""Pandas for Data Manipulation

# Python Pandas

*   Pandas stands for **Panel Data** and is the core library for data manipulation and data analysis
*   It consists of *single* and *multi-dimensional* data structures for data manipulation

*Vocab*
*   Single dimensional --> *Series* Object
*   Mult-dimensional --> **Data-frame**
"""

import pandas as pd # common alias

# Series object (from a list)
# 1-D labeled/indexed array

s1 = pd.Series([1, 2, 3, 4, 5])

# Changing the index
s_label = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s_label

print(s1)
print(type(s1))

print('\n Labeled Series')
print(s_label)

# Series from dictionary
pd.Series({'a':1, 'b':2, 'c':3,})

# Dataframe (2D labeled data structure)
# Comprised of rows/columns
pd.DataFrame({'Language':['Java', 'Python', 'C', 'C++'], 'Difficulty':[10, 5, 20, 15]})

# Dataframe built-in functions
data = pd.read_csv('/content/sample_data/california_housing_test.csv')

# data.head(10)

# data.tail()

data.describe()

# data.shape

# Accessing specific data points
data.iloc[100:110, 3:5] # stands for index location

# Creating subsets of data
subset = data.iloc[200:204, :3]
subset

# .loc[] method
data.loc[0:3, ('longitude', 'latitude', 'households')]

# Data Manipulation
print(data['latitude'] > 35)

print('')

data[(data['latitude'] > 35) & (data['housing_median_age'] == 30) & (data['households'] < 300)]

# Lambda Function
f = lambda x: x
data['housing_median_age'] = data['housing_median_age'].apply(f)
data.sort_values('housing_median_age')
