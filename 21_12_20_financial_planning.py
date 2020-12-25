print("Приложение для финансового планирования\n")

wage = int(input("Введите заработную плату в месяц: "))
while True:
    hypothec = int(input("Введите, какой процент(%) уходит на ипотеку: "))
    if 100 > hypothec > 0:
        break
    else:
        print(hypothec)
        print("Вы ввели некорректные данные")
while True:
    spending = int(input("Введите, какой процент(%) уходит на жизнь: "))
    if 100 > spending > 0:
        if (hypothec + spending) >= 100:
            print("Вы ввели некорректные данные")
        else:
            break
    else:
        print(spending)
        print("Вы ввели некорректные данные")
print("\n")


wage_year = wage * 12
hypothec_year = int(wage_year * hypothec / 100)
spending_year = int(wage_year * spending / 100)
print("Вывод: ")
print("На ипотеку было потрачено: ", hypothec_year, "рублей")
print("Было накоплено: ", wage_year - hypothec_year - spending_year, "рублей")