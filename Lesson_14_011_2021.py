from pprint import pprint
courses_list = []
course_dict = {"name":"Java-разработчик с нуля", "duration":11, "mentors":["Павел Дерендяев", "Филипп Воронов", "Анна Юшина"]}
courses_list.append(course_dict)
course2_dict = {"name":"Frontend-разработчик с нуля", "duration":13, "mentors":["Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая"]}
courses_list.append(course2_dict)
course3_dict = {"name":"Веб-разработчик с нуля", "duration":18, "mentors":["Николай Лопин", "Алена Батицкая", "Ильназ Гильязов", "Александр Шлейко", "Владимир Языков"]}
courses_list.append(course3_dict)
pprint(courses_list)

mentors_count = 0
course_id = -1
for id, course in enumerate(courses_list):
	if len(course["mentors"]) > mentors_count:
		mentors_count = len(course["mentors"])
		course_id = id
print(f'Самый крутой курс: {courses_list[course_id]["name"]}, в нем {mentors_count} преподавателей')

for course in courses_list:
	# course.setdefault("for_who", [])
	if "for_who" not in course:
			course["for_who"] = []

pprint(courses_list)

java_set = set(courses_list[0]["mentors"])
frontend_set = set(courses_list[1]["mentors"])
web_set = set(courses_list[2]["mentors"])
all_mentors_set = java_set | frontend_set | web_set
universal_soldier_set = frontend_set & web_set
# pprint(f"Всего у нас {len(all_mentors_set)} преподавателей, их список: {all_mentors_set}")
pprint(f"Всего у нас {len(universal_soldier_set)} пересекающихся преподавателей, их список: {universal_soldier_set}")

print(f"Разность Frontend и Web: {frontend_set - web_set}")
print(f"Разность Web и Frontend: {web_set - frontend_set}")
print(f"Разность Web и Frontend: {web_set.difference(frontend_set)}")
print(f"\n Симметрическая разность Frontend и Web: {frontend_set ^ web_set}")
print(f"Симметрическая разность Web и Frontend: {web_set.symmetric_difference(frontend_set)}")

test_set = java_set
test_set |= frontend_set | web_set
print()
print(test_set)

# сокращенная запись: |=, &=, ^= -=

set_list = []
for course in courses_list:
	set_list.append(set(course["mentors"]))

print("Как вытащить всех менторов в множества")
pprint(set_list)