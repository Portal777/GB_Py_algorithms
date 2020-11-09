# -*- coding: utf-8 -*-

"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
"""
import cProfile


def sieve_erat(x):
    n = 1000000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    result = []

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2
            result.append(i)

            if x == len(result):
                return result[-1]

            while j < n:
                sieve[j] = 0
                j += i
        # if x == len(result):
        #     return result[-1]

#  78498    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#  до миллиона это последнее по счету простое число

print(sieve_erat(1))
print(sieve_erat(2))
print(sieve_erat(4))
print(sieve_erat(5))
print(sieve_erat(1))
print(sieve_erat(78498))
# print(cProfile.run('sieve_erat(50000)'))

# cProfile
# 7 function calls in 0.075 seconds - 5
# 8923 function calls in 0.265 seconds - 1000
# 114733 function calls in 0.325 seconds - 10000
# 661957 function calls in 0.404 seconds - 50000
# 1078485 function calls in 0.454 seconds - 78498

# timeit
# 10 loops, best of 3: 233 msec per loop - "les4_task_1.sieve_erat(5)"
# 10 loops, best of 3: 333 msec per loop - "les4_task_1.sieve_erat(100)"
# 10 loops, best of 3: 406 msec per loop - "les4_task_1.sieve_erat(10000)"
# 10 loops, best of 3: 495 msec per loop - "les4_task_1.sieve_erat(50000)"
# 10 loops, best of 3: 501 msec per loop - "les4_task_1.sieve_erat(78498)"


# Строки 33-34 поместил внутрь проверки числа и моментального вывода, если запрашиваемое число соответствует длине
# 15 function calls in 0.132 seconds - print(cProfile.run('sieve_erat(5)'))
# 100005 function calls in 0.337 seconds print(cProfile.run('sieve_erat(50000)'))
# 157001 function calls in 0.373 seconds - print(cProfile.run('sieve_erat(78498)'))

# "les4_task_1.sieve_erat(5)"
# 10 loops, best of 3: 226 msec per loop
# "les4_task_1.sieve_erat(50000)"
# 10 loops, best of 3: 438 msec per loop
# "les4_task_1.sieve_erat(78498)"
# 10 loops, best of 3: 470 msec per loop

# Возможно это Логарифмическая сложность алгоритма O(log n) - так как n увеличивается в 10 тысяч раз, а время
# выполнения всего в 2-3 раза
