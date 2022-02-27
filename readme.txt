python
import sort
my_list = list(range(1,1000))
my_sort = sort.Sort(my_list)
my_sort.sort_len()
my_sort.sort_max()
my_sort.filter_max()
[(elem.number,elem.collatz_max) for elem in my_sort.filter_max()]
