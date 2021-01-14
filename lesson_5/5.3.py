"""Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников"""

with open("text_3.txt", encoding="utf-8") as t_3:
    list_lines = t_3.readlines()
    sum_salary = 0
    for i in range(len(list_lines)):
        sum_salary += float(list_lines[i].split()[1])
        if float(list_lines[i].split()[1]) < 20000:
            print(list_lines[i].split()[0])

average_value = sum_salary / len(list_lines)
print(average_value)
