""" Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для
пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
уроке знания: реализовать абстрактные классы для основных классов проекта, проверить
на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc_cloth(self):
        pass


class Sum(Clothes):

    def __init__(self, sum_c):
        self.sum_c = sum_c

    def __str__(self):
        return f"Всего необходимо ткани: {self.sum_c}"

    @property
    def calc_cloth(self):
        return self.sum_c

    def __add__(self, other):
        return Sum(self.calc_cloth + other.calc_cloth)


class Costume(Sum):

    def __init__(self, h):
        self.h = h

    @property
    def calc_cloth(self):
        return round(2*self.h + 0.3)


class Coat(Sum):

    def __init__(self, v):
        self.v = v

    @property
    def calc_cloth(self):
        return round(self.v/6.5 + 0.5, 2)


coat_1 = Coat(40)
coat_2 = Coat(50)
costume_1 = Costume(1.8)
costume_2 = Costume(1.7)
print(coat_1.calc_cloth)
print(costume_1.calc_cloth)
print(coat_2.calc_cloth)
print(coat_1 + costume_1 + coat_2 + costume_2)
