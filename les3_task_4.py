"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

my_list = [randint(1, 5) for i in range(10)]
my_list.sort()
print(my_list)

my_dict = {}
for i in list(set(my_list[:])):
    my_dict.update({i: my_list.count(i)})
print(my_dict)

max_num = max(my_dict, key=my_dict.get)  # ищем первое максимальное значение ключа и присваиваем ключ
value_max_num = my_dict.get(max_num)  # присваиваем значению по ключу выше

del my_dict[max_num]  # удаляем первый ключ с максимальным значением

# повторно ищем ключ с максимальным значением и присваиваем новым переменным
new_max_num = max(my_dict, key=my_dict.get)
new_value_max_num = my_dict.get(new_max_num)

print(f'Число {max_num} встречается чаще всего ({value_max_num})' if new_value_max_num < value_max_num
      else 'Такого числа нет')  # уже позже увидел условие по взятие любого первого элемента из одинаковых, оставил так
