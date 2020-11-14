"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
# 3.6.9 (default, Oct  8 2020, 12:12:24)
# [GCC 8.4.0] linux

from random import randint
import sys

my_list = [randint(1, 5) for i in range(10)]
my_list.sort()
# print(my_list)

my_dict = {}
for i in list(set(my_list[:])):
    my_dict.update({i: my_list.count(i)})
# print(my_dict)

max_num = max(my_dict, key=my_dict.get)
value_max_num = my_dict.get(max_num)

del my_dict[max_num]

new_max_num = max(my_dict, key=my_dict.get)
new_value_max_num = my_dict.get(new_max_num)

# print(f'Число {max_num} встречается чаще всего ({value_max_num})' if new_value_max_num < value_max_num
#       else 'Такого числа нет')

objects_list = list(locals().items())

objects_sizes = 0
for i in objects_list:
    if not i[0].startswith('__'):
        print(f'{i[0]} (значение -  {i[1]}) : занимает {sys.getsizeof(i[1])} байт')
        objects_sizes += sys.getsizeof(i[1])

print(f'\n***Переменные (вместе с импортом модулей) занимают - {objects_sizes} байт***')
