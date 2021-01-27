my_integer = 10
my_float = 5.5
my_bool = True
my_str = 'Hello world'

# print(type(my_integer))
# print(type(my_float))
# print(type(my_bool))
# print(type(my_str))

# print(type(4==2))

# salary = 1000
# print('Ваша годовая зарплата составляет ' + str(salary) + ' уе')

# print(True + True)

# print(20 / 5)

# print(my_str.upper())
# print(my_str.lower())
# print(my_str.title())
# print(my_str.capitalize())
# print(my_str.replace('Hello', 'Goodbye'))

# print(len(my_str))

# print(my_str)

# name = 'oleg'
# lang = 2141.124124214

# res = f'Hello, my name is {name.title()}, i know {lang :.2f} a bit'
# print(res)

# my_str = 'Hello world'
# print(my_str[2])
# print(my_str[-4])
# print(my_str[:5])
# print(my_str[1:5])
# print(my_str[0:8:2])
# print(my_str[6:])
# print(my_str[1:-3])
# print(my_str[::-1])

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]

# print(month_list[1:5])
# print(month_list[-2])

# print(income_by_months[:2][0][1])

# income_list[0] = 13500
# print(income_list)

# my_str[0] = 'R'
# print(my_str)

# print(month_list + ['erohroiujh'])

# del(income_by_months[-1])
# print(income_by_months)

# res = month_list.remove('Sep')
# print(res)
# print(month_list)
# month_list.append('Oct')
# print(month_list)

# a = [1, 2 ,3]
# b = a
# b.append(4)
# print(a)
# print(b)

# b = a[:]

# b = a.copy()

# month_list.insert(2, 'blahblahblah')
# print(month_list)


# print(month_list.sort())

# sorted(month_list)
# print(sorted(month_list))

# res = sorted(month_list)
# print(res)


# queries_string = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"

# # print(queries_string.split(','))

# print('!'.join(['Столбец 1', 'Столбец 2',   'Столбец 3']))

# salary_tuple = (1000, 1200, 1300, 900, 800)

# salary_tuple[0] = 1200

salary_tuple = ([1,2], [123])
# print(salary_tuple)

# tuple_1 = (1,)
# print(type(tuple_1))

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]

# print(zip(month_list, income_list))

# print('Jan' in month_list)

# if 'Jan' in month_list:

# else:

x = 7
while True:
    if x % 2 == 0:
        print(x, '- четное число')
    else:
        print(x, '- нечетное число')
    x -= 1
    if x == 2:
      break


# company_name = 'Orange'

# for letter in company_name:
#   print(letter)
#   letter = letter.capitalize()
#   print(letter)

companies_capitalization = [
 ['Orange', 1.3],
 ['Maxisoft', 1.5],
 ['Headbook', 0.8],
 ['Nicola', 2.2]
]

# for company in companies_capitalization:
#   # print(company)
#   print(f"{company[0]}'s cap is {company[1]} dollars")

# for name, cap in companies_capitalization:
#   # print(company)
#   print(f"{name}'s cap is {cap} dollars")

# el_1, el_2 = ['Orange', 1.3]
# print(el_1)
# print(el_2)

professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]

# print(list(zip(professions, persons)))
# for el in zip(professions, persons):
#   # print(el)
#   print(el[0], ':', sep='')
#   for name in el[1]:
#     print(name)
#   print()

phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'


# for letter in phrase:
#     if letter == ' ':
#         break
#     print(letter)
# print('finish loop')

# for letter in phrase:
#     if letter == ' ':
#         continue
#     print(letter)
# print('finish loop')

# for letter in phrase:
#     if letter == ' ':
#         pass
#     print(letter)
# print('finish loop')



