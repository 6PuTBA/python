"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import json

with open("text_7.txt", encoding="utf-8") as t_7:
    my_dict = dict()
    my_list = t_7.readlines()
    for i in my_list:
        my_dict.update({i.split()[0]: int(i.split()[-2]) - int(i.split()[-1])})
avr = 0
av_sum = 0
for i in my_dict.values():
    if i > 0:
        avr += 1
        av_sum += i
average_dict = {"average_profit": av_sum // avr}
all_list = [my_dict, average_dict]
with open("text_77.json", "w", encoding="utf-8") as t_7j:
    json.dump(all_list, t_7j, ensure_ascii=False)

print(all_list)
