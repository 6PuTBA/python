"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой."""


def users(name, surname, birthday, city, email, phone_num):
    return f"{name} {surname} {birthday} {city} {email} {phone_num}"


print(users(name="Andrey", surname="Sinitsyn", birthday="18 october", city="Moscow",
      email="andrey-sin@ya.ru", phone_num="8(999)999-99-99"))
