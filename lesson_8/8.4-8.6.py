"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


class Storage:

    max_el = 10
    storage = {}

    @classmethod
    def remaining_space(cls):
        return f"На складе осталось {cls.max_el - len(cls.storage)} мест"

    @classmethod
    def delivery(cls):
        c = input("Введите id оргтехники для выдачи: ")
        try:
            c = int(c)
            cls.storage.pop(c)
        except (ValueError, KeyError):
            print(f"Неверно введен id. На складе на данный момент есть: \n {cls.storage}")
            cls.delivery()

class Office_eq:

    id = 1

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def allocation(self):
        a = input(f"Хотите убрать {self.type} {self.name} {self.model} на склад или отнести в подразделение?")
        if "Склад" in a or "склад" in a:
            if len(Storage.storage) < Storage.max_el:
                Storage.storage.update({Office_eq.id: (self.type, self.name, self.model)})
                Office_eq.id += 1
            else:
                print("Склад заполнен")
        else: Office_eq.subdivision()

    @staticmethod
    def subdivision():
        subdiv = ["бухгалтерия", "маркетинг", "центральный офис"]
        b = input(f"Выберете подразделение из списка:{subdiv} ")
        if b in subdiv:
            print(f"Отлично, уже несем в {b}")
        else:
            print("Не понятно")
            Office_eq.subdivision()



class Printer(Office_eq):

    type = "принтер"


class Scaner(Office_eq):

    type = "сканер"


class Xerox(Office_eq):

    type = "ксерокс"


printer_1 = Printer("Canon", "3411")
printer_2 = Printer("Samsung", "m2020")
scaner_1 = Scaner("Samsung", "scx-4200")
scaner_2 = Scaner("Xerox", "7600")
xerox_1 = Xerox("Canon", "3125i")
xerox_2 = Xerox("Canone", "xr")
printer_1.allocation()
scaner_1.allocation()
xerox_1.allocation()
print(Storage.storage)
print(Storage.remaining_space())
Storage.delivery()
print(Storage.storage)






