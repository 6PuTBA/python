""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            print(*el)
        return ""

    # def __add__(self, other):
    #     """Реализация с возможностью сложения матриц с разным колличеством строк и столбцов
    #     Вроде математически сложение не равных матриц невозможно.
    #     Но долго пытался реализовать, не стал удалять"""
    #     new_matrix = []
    #     max_el = 0
    #     if len(self.matrix) > len(other.matrix):
    #         other.matrix += [[]] * (len(self.matrix) - len(other.matrix))
    #     if len(other.matrix) > len(self.matrix):
    #         self.matrix += [[]] * (len(other.matrix) - len(self.matrix))
    #     for i in range(len(self.matrix)):
    #         tmp = []
    #         if len(self.matrix[i]) > len(other.matrix[i]):
    #             if len(self.matrix[i]) > max_el:
    #                 max_el = len(self.matrix[i])
    #             other.matrix[i] += [0] * (max_el - len(other.matrix[i]))
    #         if len(other.matrix[i]) > len(self.matrix[i]):
    #             if len(other.matrix[i]) > max_el:
    #                 max_el = len(other.matrix[i])
    #             self.matrix[i] += [0] * (max_el - len(self.matrix[i]))
    #         for j in range(len(self.matrix[i])):
    #             tmp.append(self.matrix[i][j] + other.matrix[i][j])
    #         new_matrix.append(tmp)
    #     return Matrix(new_matrix)

    def __add__(self, other):
        """Реализация через обработку исключений. Возможность сложения
        только матрицы с равным колличеством строк и столбцов"""
        try:
            new_matrix = []
            for i in range(len(self.matrix)):
                tmp = []
                for j in range(len(self.matrix[i])):
                    tmp.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(tmp)
            return Matrix(new_matrix)
        except IndexError:
            return "Колличество строк и столбцов в матрице должно быть равно"


matrix_1 = Matrix([[3, 5, 32], [2, 4, 6]])
matrix_2 = Matrix([[3, 5, 0], [8, 3, 7]])
print(matrix_1.matrix)
print(matrix_1)
print(matrix_1 + matrix_2)
