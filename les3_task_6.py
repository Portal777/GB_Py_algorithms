"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

a = [randint(0, 10) for i in range(0, 10)]
# a = [0, 10, 3, 10, 9, 3, 7, 2, 9, 6]
# a = [5, 10, 0, 4, 8, 0, 1, 8, 5, 1]
print(a)

max_e = a.index(max(a))
min_e = a.index(min(a))

print(f'min #: {min_e + 1}, max #: {max_e + 1}')

if max_e < min_e:
    print(sum(a[max_e + 1:min_e]))
else:
    print(sum(a[min_e + 1:max_e]))

# два часа спустя я потерял желание разбираться в этом ...
#
# if max_e + 1 != min_e and max_e - 1 != min_e:
#     if max_e < min_e:
#         print(sum(a[max_e + 1:min_e]))
#     else:
#         print(sum(a[min_e + 1:max_e]))
#
#
# else:
#     if max_e < min_e:
#         max_e = a.index(max(a[:max_e] + a[max_e + 1:]))
#         print(sum(a[max_e + 1:min_e]))
#     else:
#
#         if max_e != len(a):
#             new_max_e = 0
#             for i, e in enumerate(a):
#                 if e == max((a[:max_e] + a[max_e + 1:])):
#                     if e > max_e:
#                         new_max_e = i + 1
#                     else:
#                         new_max_e = i - 1
#
#             print(sum(a[min_e + 1:new_max_e]))
#         else:
#             new_max_e = a.index(max(a[:max_e]))
#             print(sum(a[min_e + 1:new_max_e]))
#         print(f'new max #: {new_max_e}')
