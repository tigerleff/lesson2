# Задание 2 if
# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.


def func(string1, string2):
    if string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 and  string2 == 'learn':
        return 3

string1 = input('Введите значение string1 ')
string2 = input('Введите значение string2 ')

print(func(string1, string2))
