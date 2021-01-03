"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее."""

from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

с = 0
my_list = [1, 2, 3, 4, 5]
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1