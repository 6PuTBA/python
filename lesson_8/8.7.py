"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата"""


class Complex_num:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)


num_1 = Complex_num(5, 6)
num_2 = Complex_num(7, 8)
print(num_1+num_2)
print(num_1*num_2)


class Complex_num_1:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{self.a}"

    def __add__(self, other):
        return Complex_num_1(self.a + other.a)

    def __mul__(self, other):
        return Complex_num_1(self.a * other.a)

num_3 = Complex_num_1(complex(5, 6))
num_4 = Complex_num_1(complex(7, 8))
print(num_3+num_4+num_4)
print(num_3*num_4*num_4)



