# -*- coding: utf-8 -*-
"""Flow Control

# **If** statement

## Tuples
"""

tup1 = ('a', 'b', 1, 2, 3)
if 'a' in tup1:
  print("The letter 'a' is in the tuple")

"""## Lists"""

lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if lis1[0] == 1:
  lis1[0] = 100
print(lis1)

"""## Dictionaries"""

d1 = {'a' : 'first letter', 'b' : 2, 'c' : True}
if d1['b'] == 2:
  d1['b'] = False
d1

"""# **Looping** Statements"""

l1 = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(l1):
  l1[i] += 100
  i += 1

l1

for i in range(len(l1)):
  l1[i] += 100

l1

colors = ['blue', 'red', 'yellow', 'green']
furniture = ['chair', 'sofa', 'desk']

print('Possible items: \n ')
for color in colors:
  for thing in furniture:
    print(f'{color} {thing}')
