python
import sort
my_list = list(range(1,1000))
my_sort = sort.Sort(my_list)
my_sort.sort_max()
[(elem.number,elem.collatz_max) for elem in my_sort.sorted_list]
[elem.collatz_max for elem in my_sort.sorted_list]
list(dict.fromkeys([elem.collatz_max for elem in my_sort.sorted_list]))
