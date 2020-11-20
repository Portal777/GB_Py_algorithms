"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

***WIKI
Для решения задачи сортировки эти три этапа выглядят так:

Сортируемый массив разбивается на две части примерно одинакового размера;
Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
Два упорядоченных массива половинного размера соединяются в один.

1.1. — 2.1. Рекурсивное разбиение задачи на меньшие происходит до тех пор, пока размер массива не достигнет единицы
(любой массив длины 1 можно считать упорядоченным).

3.1. Соединение двух упорядоченных массивов в один.
Основную идею слияния двух отсортированных массивов можно объяснить на следующем примере. Пусть мы имеем два уже
отсортированных по возрастанию подмассива. Тогда:
3.2. Слияние двух подмассивов в третий результирующий массив.
На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив.
Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
3.4. «Прицепление» остатка.
Когда один из подмассивов закончился, мы добавляем все оставшиеся элементы второго подмассива в результирующий массив.

"""

from random import randint
import cProfile

my_array = [randint(0, 50) for i in range(15)]


def sort_func(array):
    if len(array) <= 1:
        return "Список не нуждается в сортировке"
    new_array = [list(i for i in array[:len(array) // 2]), list(i for i in array[len(array) // 2:])]
    # while len(new_array) != 2:
    #     pass

    return new_array


# print(my_array)
print(sort_func(my_array))

# cProfile.run('sort_func(my_array)')
