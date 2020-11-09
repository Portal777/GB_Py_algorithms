# -*- coding: utf-8 -*-
"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import cProfile

def sieve_erat(x):
    result = []
    n = 1000000
    sieve = [i for i in range(2, n)]
    for i in sieve:
        if len(result) == x:
            return result[-1]
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            result.append(i)


print(sieve_erat(2))
print(sieve_erat(4))
print(sieve_erat(5))
print(sieve_erat(1))
print(sieve_erat(2000))
# print(sieve_erat(78498))

# print(cProfile.run('sieve_erat(100000)'))
# 44 function calls in 0.050 seconds - print(cProfile.run('sieve_erat(10)'))
# 646 function calls in 0.053 seconds - print(cProfile.run('sieve_erat(100)'))
# 8924 function calls in 0.279 seconds - print(cProfile.run('sieve_erat(1000)'))
# 53616 function calls in 6.573 seconds - print(cProfile.run('sieve_erat(5000)'))
# 114734 function calls in 31.552 seconds - print(cProfile.run('sieve_erat(10000)'))
# 1078501 function calls in 2283.251 seconds - print(cProfile.run('sieve_erat(100000)'))

# "les4_task_2.sieve_erat(10)"
# 10 loops, best of 3: 33.9 msec per loop
# "les4_task_2.sieve_erat(100)"
# 10 loops, best of 3: 35.1 msec per loop
# "les4_task_2.sieve_erat(1000)"
# 10 loops, best of 3: 191 msec per loop
# "les4_task_2.sieve_erat(5000)"
# 10 loops, best of 3: 4.88 sec per loop

# с таким решением, получается квадратичная сложность O(n**2)
# при увеличении n с 1000 до 5000 тысяч (в 5 раз), время выполнения увеличивается ~ в 23.5 раза
# с 5000 до 10000 (в 2 раза), время выполнения увеличивается только ~ в 4.8 раза
# с 10000 до 100000 (в 10 раз), время увеличилось ~ В 72,3 раза
