#!/usr/bin/python3

from collatz import Collatz
from operator import attrgetter

class Sort(Collatz):
   """docstring for Sort"""

   sorted_list = []

   def __init__(self, arg):
      if type(arg) == list:
         self.sorted_list = arg
         self.prepare_collatz_list()
         self.sort_len()
      if type(arg) == type(self):
         print('arg is ', type(self))
         self.number = arg.number
         self.collatz_list = arg.collatz_list

   def prepare_collatz_list(self):
      while type(self.sorted_list[0]) != Collatz:
         current_number = self.sorted_list[0]
         current_collatz = Collatz(current_number)

         peer_list     = [current_collatz for elem in self.sorted_list if elem == current_number]
         remaimed_list = [elem            for elem in self.sorted_list if elem != current_number]

         self.sorted_list = remaimed_list + peer_list

   def get_me(self):
      return [elem.get_me() for elem in self.sorted_list]

   def sort_len(self):
      self.sorted_list = sorted(self.sorted_list, key = attrgetter('number'))
      self.sorted_list = sorted(self.sorted_list, key = attrgetter('collatz_length'))

   def sort_max(self):
      self.sorted_list = sorted(self.sorted_list, key = attrgetter('number'))
      self.sorted_list = sorted(self.sorted_list, key = attrgetter('collatz_max'))

   def filter_max(self):
      filtered_max = []
      self.sort_max()
      token_max_list = list(dict.fromkeys([elem.collatz_max for elem in self.sorted_list]))
      for token_max in token_max_list:
         token_filtered_max_list = [elem for elem in self.sorted_list if elem.collatz_max == token_max]
         filtered_max =  filtered_max + [token_filtered_max_list[-1]]
      return filtered_max

   def __repr__(self):
      return repr(vars(self))
