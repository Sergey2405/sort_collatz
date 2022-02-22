#!/usr/bin/python3

from collatz import Collatz


class Sort(Collatz):
   """docstring for Sort"""

   sort_list = []

   def __init__(self, arg):
      if type(arg) == list:
         self.sort_list = arg
         self.prepare_collatz_list()
         self.sort()
      if type(arg) == type(self):
         print('arg is ', type(self))
         self.number = arg.number
         self.collatz_list = arg.collatz_list
      self.arg = arg

   def prepare_collatz_list(self):
      self.sort_list = self.__prepare_collatz_list(self.sort_list)

   def get_me(self):
      return [elem.get_me() for elem in self.sort_list]

   def sort(self):
      self.sort_list =  self.__do_sort_collatz(self.sort_list)

   def __prepare_collatz_list(self, number_list):
      if number_list == []:
           return []

      current_number = number_list[0]
      current_collatz = Collatz(current_number)

      peer_list     = [current_collatz for elem in number_list if elem == current_number]
      remaimed_list = [elem            for elem in number_list if elem != current_number]

      if number_list == []:
         return []
      else:
         # return self.__prepare_collatz_list(remaimed_list) + peer_list
         return peer_list + self.__prepare_collatz_list(remaimed_list)

   def __do_sort_collatz(self, sort_list):

      if sort_list == []:
         return []

      current_collatz = sort_list[0]
      current_number = current_collatz.number
      current_length = current_collatz.collatz_length

      peer_list          = [elem for elem in sort_list if elem.number == current_number and elem.collatz_length == current_length]
      peer_low_unsorted  = [elem for elem in sort_list if elem.number < current_number and elem.collatz_length == current_length]
      peer_high_unsorted = [elem for elem in sort_list if elem.number > current_number and elem.collatz_length == current_length]

      low_unsorted    =    [elem for elem in sort_list if elem.number != current_number and elem.collatz_length < current_length]
      high_unsorted   =    [elem for elem in sort_list if elem.number != current_number and elem.collatz_length > current_length]
      
      return self.__do_sort_collatz(low_unsorted) + self.__do_sort_collatz(peer_low_unsorted) + peer_list + \
             self.__do_sort_collatz(peer_high_unsorted) + self.__do_sort_collatz(high_unsorted)
