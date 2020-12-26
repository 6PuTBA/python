"""Реализовать функцию my_func(), которая принимает три позиционных
 аргумента, и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    if a > c:
        return max(b, c) + a
    else:
        return max(b, a) + c


print(my_func(int(input("a=")), int(input("b=")), int(input("c="))))
