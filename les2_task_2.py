"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count(num):
    def_num = num
    even = ''
    uneven = ''

    while num > 0:
        digit = num % 10  # можно обойтись без данной переменной, но для наглядности оставил

        if digit % 2 == 0:
            even = f'{str(digit)} {even}'
        else:
            uneven = f'{str(digit)} {uneven}'

        num //= 10

    return f'В числе {def_num}: {len(even.replace(" ", ""))} четные цифры ({even.strip()}) ' \
           f'и {len(uneven.replace(" ", ""))} нечетные ({uneven.strip()})'


print(count(int(input('Введите натуральное число: '))))
