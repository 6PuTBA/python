dohod = int(input("Введите выручку вашей компании: "))
rashod = int(input("Введите издержки вашей компании: "))
if dohod > rashod:
    profit = dohod - rashod
    rent = (profit / dohod) * 100
    print(f"Поздравляем! Ваша компания прибыльна! Рентабелльность вашей фирмы составила {rent:.0f}%")
    sotrudniki = int(input("Сколько же у вас работает сотрудников? "))
    print(f"Каждый сотрудник вашей компании заработал по {profit // sotrudniki} rub")
else:
    print("К сожалению ваша компания отработала в убыток")