class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_bm(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def __str__(self, student):

    # def some_student(self, student):


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):

        if isinstance(student,
                      Student) and course in self.courses_attached and course \
                in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return


eman_student = Student('Ruoy', 'Eman', 'your_gender')
eman_student.finished_courses += ['Git']
# eman_student.courses_in_progress += ['Python']
eman_student.grades['Git'] = [10, 10, 10, 10, 10]
# eman_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
budy_lecturer = Lecturer('Some', 'Buddy')
budy_lecturer.courses_attached += ['Python']
budy_lecturer.grades['Python'] = []

eman_student.rate_bm(budy_lecturer, 'Python', 10)
# best_student.rate_bm(budy_lecturer, 'Python', 10)
# best_student.rate_bm(budy_lecturer, 'Python', 10)
#
print(budy_lecturer.courses_attached)
print(budy_lecturer.grades)
#
# assessment_reviewer = Reviewer('Peter', 'Jones')
#
# assessment_reviewer.rate_hw(best_student, 'Python', 10)
# assessment_reviewer.rate_hw(best_student, 'Python', 10)
# assessment_reviewer.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
