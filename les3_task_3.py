"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint

my_list = [randint(-20, 20) for i in range(0, 6)]

copy_list = my_list[:]

result_list = my_list[:]
result_list.sort()

print(my_list)

my_list[copy_list.index(result_list[0])], my_list[copy_list.index(result_list[-1])] \
    = my_list[copy_list.index(result_list[-1])], my_list[copy_list.index(result_list[0])]

print(my_list)
