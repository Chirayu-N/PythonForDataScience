# -*- coding: utf-8 -*-
"""
# Matplotlib
*   Matplotlib is a Python library used for data **visalization**
*   Can create bar graphs, scatter-plots, histograms, and more
"""

# Commented out IPython magic to ensure Python compatibility.
from matplotlib import pyplot as plt
# %matplotlib inline # Formatting for Jupyter Notebook

# Other libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Data for line plot
x = np.arange(1, 11)
y1 = 2 * x
y2 = 3 * x

# Creating the plot
plt.plot(x, y1, color='red', linewidth = '3', linestyle=':')
plt.plot(x, y2, color='blue', linewidth = '3', linestyle=':')

plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()

plt.show()

# Data for bar plot
p_lang = {
    'Python' : 10,
    'Java' : 30,
    'C++' : 40,
    'C': 55
}

languages = list(p_lang.keys())
difficulty = list(p_lang.values())

# Creating the bar plot
plt.bar(languages, difficulty, color='black')
# plt.barh(languages, difficulty, color='black')

plt.title('Programming language vs. difficulty')
plt.xlabel('Language')
plt.ylabel('Difficulty')
# plt.grid()

plt.show()

# Data for scatterplot
x = np.random.rand(100)
y1 = np.random.rand(100)
y2 = np.random.rand(100)

# Creating the plot
plt.scatter(x, y1)
plt.scatter(x, y2)

plt.grid()

plt.show()

# Data for Histogram/Boxplot
path = '/content/sample_data/california_housing_test.csv'
cdata = pd.read_csv(path)

# print(cdata.head())
# print('\n' * 3)

# Creating the histogram
plt.hist(cdata['median_income'], bins=20)

plt.title('Median income of California house owners')
plt.xlabel('Income')
plt.ylabel('Frequency ')
plt.grid()

plt.show()

# Boxplot
path2 = '/content/drive/My Drive/10th Grade/Other/Python/Python for Data Science/Iris.csv'
iris = pd.read_csv(path2)

iris.boxplot(column='SepalLengthCm', by='Species')
plt.show()
print('\n' * 3)

# Using Seaborn library
print('Seaborn')
sns.set(style='dark')
sns.boxplot(x=iris['Species'], y=iris['SepalLengthCm'])
plt.show()

# Pie Chart

# Data
fruit = ['Python', 'Java', 'C', 'C++']
cost = np.random.randint(1, 50, 4)
