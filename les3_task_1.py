"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
result = [[] for _ in range(8)]

for num in range(2, 100):
    for digit in range(2, 10):
        result[digit-2].append(num) if num % digit == 0 else 'None'

for answ in result:
    # print(answ)
    print(f'Кратных числу {result.index(answ)+2} = {len(answ)}')
