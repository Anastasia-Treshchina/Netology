print("Знаки Зодиака. \n\n Инструкция по применению \n для определения "
      "своего знака Зодиака:\n 1. Введите день в числовом формате. \n 2. "
      "Enter. \n 3. Введите месяц в цифровом формате.\n 4. Enter.\n")

while True:
    day = int(input("Введите день рождения: "))
    if 1 <= day <= 31:
        month = int(input("Введите месяц рождения: "))
        if 1 <= month <= 12:
            if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and
                                                    month == 4):
                print("\nВаш знак зодиака Овен! \n")
            elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and
                                                      month == 5):
                print("\nВаш знак зодиака Телец!\n")
            elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and
                                                      month == 6):
                print("\nВаш знак зодиака Близнецы!\n")
            elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and
                                                      month == 7):
                print("\nВаш знак зодиака Рак!\n")
            elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and
                                                      month == 8):
                print("\nВаш знак зодиака Лев!\n")
            elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and
                                                      month == 9):
                print("\nВаш знак зодиака Дева!\n")
            elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and
                                                      month == 10):
                print("\nВаш знак зодиака Весы!\n")
            elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and
                                                       month == 11):
                print("\nВаш знак зодиака Скорпион!\n")
            elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and
                                                       month == 12):
                print("\nВаш знак зодиака Стрелец!\n")
            elif (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and
                                                       month == 1):
                print("\nВаш знак зодиака Козерог!\n")
            elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and
                                                      month == 2):
                print("\nВаш знак зодиака Водолей!\n")
            elif (30 <= day <= 31 and month == 2) or (day == 31 and month == 4) \
                    or (day == 31 and month == 6) or (day == 31 and month == 9) \
                    or (day == 31 and month == 11):
                print("\nВы ввели некорректную дату!\n")
            elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and
                                                      month == 3):
                print("\nВаш знак зодиака Рыбы!\n")
        else:
            print("\nВведите число от 1 до 12\n")
    else:
        print("\nВведите число от 1 до 31\n")
