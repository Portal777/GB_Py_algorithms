"""
Определить, является ли год, который ввел пользователь, високосным или не високосным
"""
from calendar import isleap

user_year = int(input("Введите год в формате YYYY: "))

if isleap(user_year):
    print("Год високосный")
elif not isleap(user_year):
    print("Год не високосный")
