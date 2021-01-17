""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат."""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула "
              f"{'налево' if direction == 'лево' else 'направо' if direction == 'право' else 'непойми куда'}")

    def show_speed(self):
        print(f"Скорость движения автомобиля: {self.s}км/ч")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость движения автомобиля: {self.s}км/ч")
        if self.s > 60:
            print("Скорость превышена, снизтесь до 60")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость движения автомобиля: {self.s}км/ч")
        if self.s > 40:
            print("Скорость превышена, снизтесь до 40")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(speed=110, color="Blue", name="Logan")
ikea = WorkCar(speed=70, color="Blue", name="Transporter")
f1 = SportCar(speed=330, color="Red", name="Ferarri")
town_car = TownCar(speed=70, color="Black", name="Ceed")
print(police.c)
f1.show_speed()
ikea.show_speed()
print(town_car.p)
f1.turn('ррозо')
