# -*- coding: utf-8 -*-
"""Numerical Computing with Numpy

# NumPy

*   NumPy stands for **Numerical Python** and is the core library for numeric and scientific computing
*   It consists of **multi-dimensional array objects** and a collection of routines (methods) for processing those arrays
"""

import numpy as np # alias for numpy

# Single Dimensional
n1 = np.array([1, 2, 3, 4, 5])
print (n1)
print('\n')

# Multi-dimensional
n2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n2)

# Initializing NumPy Array

# Zeros
n0 = np.zeros((3, 7))
print(n0)
print('')

# Other number
n17 = np.full((3, 7), 17)
print(n17)
print('')

# In a range
nrange = np.arange(10, 105, 10)
print(nrange)
print('')

# Random numbers
nrandom = np.random.randint(1, 100, 5)
print(nrandom)

# NumPy Shape
n0.shape

# Array Addition
total = np.sum([n1, nrandom])
vertical = np.sum([n1, nrandom], axis=0) # Adds all columns separately
horizontal = np.sum([n1, nrandom], axis=1) # Adds all rows separately

print(total)
print(vertical)
print(horizontal)

# Joining NumPy Arrays

# Vertical Stack
print(np.vstack((n1, nrandom)))
print('')

# Horizontal Stack
print(np.hstack((n1, nrandom)))
print('')

# Column Stack
print(np.column_stack((n1, nrandom)))
print('')

# Row Stack - not used because same as vertical stack
print(np.row_stack((n1, nrandom)))
print('')

# Printing random integers

# NumPy
# import numpy as np
array = np.random.randint(1, 11, 5)
for number in np.nditer(array):
  print(number)

print('')

# Random module
import random as rd
for number in range(5):
  print(rd.randint(1,10))
