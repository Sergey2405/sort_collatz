#!/usr/bin/python3
from operator import attrgetter 

class Collatz:
   """docstring for Collatz"""

   number = 0
   collatz_length = 0
   collatz_max = 0
   collatz_list = []

   def collatz(self, arg):
      self.collatz_list = self.__collatz(arg, [])

   def get_me(self):
      return (self.number, self.collatz_length, self.collatz_list)


   def __collatz(self, arg, history):
      if arg == 1:
         return history
      elif arg % 2 == 0:
         return self.__collatz(arg // 2, history + [arg])
      else:
         return self.__collatz(arg * 3 + 1, history + [arg])

   def __init__(self, arg):
      if type(arg) == int and arg > 0:
         self.number = arg
         self.collatz(arg)
         self.collatz_length = len(self.collatz_list)
         if self.collatz_list != []:
            self.collatz_max = max(self.collatz_list)
      elif type(arg) == type(self):
         print('arg is ', type(self))
         self.collatz_list = arg.collatz_list
         self.number = arg.number
      else:
         self.number = arg


   def __repr__(self):
      return repr(vars(self))
