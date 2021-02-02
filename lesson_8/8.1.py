"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:

    def __init__(self, string):
        Data.s = string

    @classmethod
    def conversion(cls):
        return list(map(int, cls.s.split("-")))

    @staticmethod
    def validation():
        if Data.conversion()[1] < 1 or Data.conversion()[1] > 12:
            return False
        if Data.conversion()[1] in (1, 3, 5, 7, 8, 10, 12):
            if Data.conversion()[0] < 1 or Data.conversion()[0] > 31:
                return False
        if Data.conversion()[1] in (4, 6, 9, 11):
            if Data.conversion()[0] < 1 or Data.conversion()[0] > 30:
                return False
        if Data.conversion()[1] == 2:
            if (Data.conversion()[2] % 4 == 0 and Data.conversion()[2] % 100 != 0) or Data.conversion()[2] % 400 == 0:
                if Data.conversion()[0] < 1 or Data.conversion()[0] > 29:
                    return False
            else:
                if Data.conversion()[0] < 1 or Data.conversion()[0] > 28:
                    return False
        return True


print(Data("18-01-1989").conversion())
print(Data("29-02-1600").validation())
