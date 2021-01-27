def square(number):
  '''
  this is my first function
  '''
  result = number ** 2
  return result

# print(square(10))
# res = square(10)
# print(square(res))
# print(res)

# sum = 10
from pprint import pprint

# help(square)

def square_2():
  number = int(input('Введите число'))
  return number ** 2

# print(square_2())

def power(number_1, number_2=2):
  result = number_1 ** number_2
  return result

# print(power(2))

def square_3(number):
  result = number ** 2
  print(result)
  # return None


# square_3(2)

number = 5
power = 10

def power_5():
  number = 6
  power = 2
  some_number = 1
  return number ** power

# print(number ** power)
# print(power_5())
# print(some_number)





name = 'James'

# def say_hi():
#   global name
#   name = 'Oleg'
#   print('Hello ', name)

# print(name)
# say_hi()

# help(len)

def say_hi():
  name = 'Oleg'
  def get_name():
    nonlocal name
    name = input('Введите имя')
    return name
  get_name()
  print('Hello', name)

# say_hi()

# my_func = lambda x, y: x + y

# print(my_func(5, 6))


students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 8, 8, 9, 8],"exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
]

# print(students_list)

def get_avg_exam_grade(students):
  sum_ex = 0
  for student in students:
    sum_ex += student['exam']
  return round(sum_ex / len(students), 2)

#print(get_avg_exam_grade(students_list))

def get_avg_hw_grade(students):
  sum_hw = 0
  for student in students:
    sum_hw += sum(student['grade']) / len(student['grade'])
  return round(sum_hw / len(students), 2)

# print(get_avg_hw_grade(students_list))

def get_avg_hw_grade(students, exp=None):
  sum_hw = 0
  counter = 0
  for student in students:
    if student['program_exp'] == exp or exp is None:
      sum_hw += sum(student['grade']) / len(student['grade'])
      counter += 1
  return round(sum_hw / counter, 2)

print(get_avg_hw_grade(students_list))
print(get_avg_hw_grade(students_list, False))
print(get_avg_hw_grade(students_list, True))


def main(students):
  while True:
    user_input = input('Введите команду')
    if user_input == '1':
      print(get_avg_exam_grade(students))
    elif user_input == '2':
      print(get_avg_hw_grade(students))
    elif user_input == '3':
      print(get_avg_hw_grade(students, False))
    elif user_input == 'q':
      break

main(students_list)

