print("Приложение для финансового планирования\n")

wage = int(input("Введите заработную плату в месяц: "))
hypothec = int(input("Введите, какой процент(%) уходит на ипотеку: "))
spending = int(input("Введите, какой процент(%) уходит на жизнь: "))
print("\n")

wage_year = wage * 12
hypothec_year = int(wage_year * hypothec / 100)
spending_year = int(wage_year * spending / 100)
print("Вывод: ")
print("На ипотеку было потрачено: ", hypothec_year, "рублей")
print("Было накоплено: ", wage_year - hypothec_year - spending_year, "рублей")
