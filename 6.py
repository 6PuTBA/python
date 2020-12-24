"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя."""

products = []
full_products = []
val_end = "y"
while val_end == "y":
    products.append({"название": input("Введите название товара: "),
                     "цена": input("Введите цену товара: "),
                     "количество": input("Введите количество товара: "),
                     "ед": input("Введите единицу измерения товара: ")})
    val_end = input("Хотите ввести еще один товар? (y/n)").lower()
for i, el in enumerate(products):
    full_products.append((i+1, el))
print(full_products)

"""Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый 
ключ — характеристика товара, например название, а значение — список значений-
характеристик, например список названий товаров."""

names = []
price = []
count = []
un = []

for i in range(len(full_products)):
    names.append(full_products[i][1].get("название"))
for i in range(len(full_products)):
    price.append(full_products[i][1].get("цена"))
for i in range(len(full_products)):
    count.append(full_products[i][1].get("количество"))
for i in range(len(full_products)):
    un.append(full_products[i][1].get("ед"))

analitic_dict = {"название": names, "цена": price, "количество": count, "ед": un}
print(analitic_dict)


