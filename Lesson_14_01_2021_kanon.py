# ДЗ можно делать на основе кода из лекции
# Задание 1. Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.
# geo_logs = [ {'visit1': ['Москва', 'Россия']} ]

# Задание 2. Выведите на экран все уникальные гео-ID из значений словаря ids. Т. е. список вида [213, 15, 54, 119, 98, 35]
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119]}

# Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них. Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
# queries = ['смотреть сериалы онлайн', 'новости спорта']

# Задание 4. Дана статистика рекламных каналов по объемам продаж. Напишите скрипт, который возвращает название канала с максимальным объемом. Т. е. в данном примере скрипт должен возвращать 'yandex'.
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# Задание 5. *(Необязательное) Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

from pprint import pprint

# КЕЙС: Анализируем курсы "Нетологии" по программированию
# проверим, какой курс самый "крутой" (больше всего преподавателей) и есть ли супер-преподаватели, которые участвуют больше чем в одном курсе

# создаем список из 3х курсов. каждый курс - это словарь. содержит название (title), список преподавателей (mentors) и продолжительность в месяцах (duration)
courses_list = [
	{
		"title":"Java-разработчик с нуля",
		"mentors": ["Павел Дерендяев", "Алексей Яковлев", "Дмитрий Гордин", "Сергей Сердюк", "Анатолий Корсаков", "Вадим Ерошевичев", "Алексей Фомичев", "Филипп Воронов"],
		"duration": 11
	},
	{
		"title":"Веб-разработчик с нуля",
		"mentors": ["Николай Лопин", "Алёна Батицкая", "Алексей Дацков", "Александр Беспоясов", "Евгений Корытов", "Алексей Кулагин", "Ильназ Гильязов", "Владимир Языков", "Владимир Чебукин", "Эдгар Нуруллин", "Александр Дудинский"],
		"duration": 19
	},
	{
		"title":"Frontend-разработчик с нуля",
		"mentors": ["Ильназ Гильязов", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алёна Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер"],
		"duration": 13
	}
]

# РАБОТА СО СЛОВАРЯМИ
# 1) смотрим преподавателей каждого курса (работа со словарем)
for course in courses_list:
	print("Название курса: {}".format(course["title"]))
	print("Преподаватели курса: {}".format(", ".join(course["mentors"])))
	print()

# 2) считаем, какой курс "круче": на котором из них больше всего преподавателей?
# для этого необходимо запомнить наибольшее количество преподавателей и ID курса в списке (list) курсов
leader_id = 0
mentors_count = 0
for id, course in enumerate(courses_list):
	if len(course["mentors"]) > mentors_count:
		mentors_count = len(course["mentors"])
		course_id = id
print(f'Самый крутой курс: {courses_list[course_id]["title"]}, в нем {mentors_count} преподавателей')

# 3) Если мы обнаружили, что нам не хватает значимой информации про курс (например, на кого он ориентирован), мы можем добавить новый ключ словаря двумя способами: ручной проверкой или через dict.setdefault:
for course in courses_list:
	course.setdefault("for_who", [])
	# if "for_who" not in course:
	# 		course["for_who"] = []

# РАБОТА С МНОЖЕСТВАМИ
# 4) смотрим, кто из преподавателей преподает на нескольких курсах (пересечение множеств)
# проверяем, что у нас такие вообще есть. для этого можно объединить всех преподавателей в список и множество и подсчитать количество человек в каждом. в множестве должно быть меньше, т.к. там нет дублирующихся людей
java_set = set(courses_list[0]["mentors"])
frontend_set = set(courses_list[1]["mentors"])
web_set = set(courses_list[2]["mentors"])
all_mentors_set = java_set | frontend_set | web_set
pprint(f"Всего у нас {len(all_mentors_set)} преподавателей, их список: {all_mentors_set}")

# смотрим, кто именно преподает несколько курсов
# при пересечении всех сразу множеств будет пустое множество set(), т.к. нет никого, кто преподавал бы сразу на трех курсах:
universal_soldier_set = java_set & frontend_set & web_set
# а вот здесь будут пересекающиеся преподаватели:
universal_soldier_set = frontend_set & web_set
pprint(f"Всего у нас {len(universal_soldier_set)} пересекающихся преподавателей, их список: {universal_soldier_set}")

# 5) проверяем, как работает разность множеств и симметрическая разность:
print(f"Разность Frontend и Web: {frontend_set - web_set}")
print(f"Разность Web и Frontend: {web_set.difference(frontend_set)}")
print(f"\n Симметрическая разность Frontend и Web: {frontend_set ^ web_set}")
print(f"Симметрическая разность Web и Frontend: {web_set.symmetric_difference(frontend_set)}")

# 6) сокращенная запись
# во всех случаях выше у нас в результате создавалось новое множество
# а вот так можно сделать, чтобы результат записывался в конкретное множество (в нашем случае test_set)
# просто используйте сокращенную запись, как в арифметических операциях: |=, &=, ^= -=
test_set = java_set
test_set |= frontend_set | web_set
print(test_set)