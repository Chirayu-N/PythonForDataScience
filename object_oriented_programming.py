# -*- coding: utf-8 -*-
"""Object Oriented Programming"""

# Functions
def even_or_odd(number):
  if number % 2 == 0:
    return 'even'
  else:
    return 'odd'

for n in range(10):
  print(f'{n} is {even_or_odd(n)}')

# Objects
class Phone:

  def make_call(self):
    print('Making a phone call')

  def play_game(self):
    print('Playing games')

iPhone = Phone() # creating an instance of the class
iPhone.play_game()

# Inheritance and methods with parameters
class Phone2(Phone):

  def add_color(self, color):
    self.color = color
  
  def add_cost(self, cost):
    self.cost = cost

  def show_color(self):
    return color
  
  def show_cost(self):
    return cost

samsung = Phone2()
samsung.make_call()
