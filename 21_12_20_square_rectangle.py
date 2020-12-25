print("Квадрат и прямоугольник\n")

side_square = int(input("Введите длину стороны квадрата: "))
print("\n")

print("Вывод:")
print("Периметр: ", side_square * 4)
print("Площадь: ", side_square ** 2, "\n")

length_rectangle = int(input("Введите длину прямоугольника: "))
heigth_rectangle = int(input("Введите ширину прямоугольника: "))
print("\n")

print("Вывод:")
print("Периметр: ", (length_rectangle + heigth_rectangle) * 2)
print("Площадь: ", length_rectangle * heigth_rectangle)