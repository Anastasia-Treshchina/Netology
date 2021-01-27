def summary_ab():
    num1 = int(input("Введите значение А = "))
    num2 = int(input("Введите значение B = "))

    amount = num1 + num2
    if 1 <= num1 <= 1000 and 1 <= num2 <= 1000:
        print(amount)
    else:
        print("Введите данные от 1 до 1000")


summary_ab()
