"""Создать текстовый файл (не программно), сохранить в нём несколько
строк, выполнить подсчёт строк и слов в каждой строке."""

with open("test_1.txt", encoding="utf-8") as t_1:
    my_list = t_1.readlines()
    print(f"В файле {len(my_list)} строк")
    for i in range(len(my_list)):
        print(f'В {i+1}-й строке {len(my_list[i].split())} слов')
