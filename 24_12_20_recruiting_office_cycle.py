print("ВОЕНКОМАТ")

while True:
    name = input("ФИО: ")
    age = int(input("Возраст: "))
    if 18 <= age < 27:
        learns = int(input("Учится (1 - да, 0 - нет)?: "))
        if learns == 0:
            children = int(input("Количество детей: "))
            if children == 0:
                height = int(input("Рост: "))
                if height < 170:
                    print("\nВ танкисты\n")
                elif height < 185:
                    print("\nНа флот\n")
                elif height < 200:
                    print("\nВ десантники\n")
                else:
                    print("\nВ другие войска\n")
            else:
                print("\nЕсть дети\n")
        else:
            print("\nОтсрочка по учебе\n")
    else:
        print("\nНепризывной возраст\n")
