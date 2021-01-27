print("ВОЕНКОМАТ")

height = int(input("Рост: "))
age = int(input("Возраст: "))
learns = int(input("Учится (1 - да, 0 - нет)?: "))
children = int(input("Количество детей: "))

if 18 <= age < 27:
  if learns == 0:
    if children == 0:
      if height < 170:
        print("В танкисты")
      elif height < 185:
        print("На флот")
      elif height < 200:
        print("В десантники")
      else:
        print("В другие войска")
    else:
      print("Есть дети")
  else:
    print("Отсрочка по учебе")
else:
  print("Непризывной возраст")

