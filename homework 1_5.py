
import sys
students = [
        {"Name":"Марина","Surname":"Тихомирова","Gender":"F","Experienced":False,
         "Homeworks":[10,5,7,3,6],"Exam":8},
        {"Name":"Кирилл","Surname":"Гончаров","Gender":"M","Experienced":True,
         "Homeworks":[9,10,10,8,9],"Exam":10},
        {"Name":"Максим","Surname":"Николаев","Gender":"M","Experienced":False,
         "Homeworks":[8,5,2,7,4],"Exam":5},
        {"Name":"Оксана","Surname":"Иванова","Gender":"F","Experienced":True,
         "Homeworks":[10,9,10,9,8],"Exam":10},
        {"Name":"Алексей","Surname":"Афонасьев","Gender":"M","Experienced":False,
         "Homeworks":[7,8,6,7,9],"Exam":7},
        {"Name":"Виктория","Surname":"Карасева","Gender":"F","Experienced":True,
         "Homeworks":[5,5,3,7,4],"Exam":5}
    ]

def count_avg_by_person(student):
        avg_homework = 0
        exam = student["Exam"]
        homework_marks = student["Homeworks"]
        count_marks = 0
        for mark in homework_marks:
            count_marks += 1
            avg_homework += mark
        avg_homework /=count_marks
        return avg_homework, exam

def count_statistic(students, option):
    avg_group1_homework = 0
    avg_group1_exam = 0
    avg_group2_homework = 0
    avg_group2_exam = 0
    if option == "Gender":
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, "M")
        avg_group2_homework, avg_group2_exam = avg_custom_group(students, option, "F")
        return avg_group1_homework, avg_group1_exam, avg_group2_homework, avg_group2_exam
    elif option == "Experienced":
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, True)
        avg_group2_homework, avg_group2_exam = avg_custom_group(students, option, False)
        return avg_group1_homework, avg_group1_exam, avg_group2_homework, avg_group2_exam
    else:
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, None)
        return avg_group1_homework, avg_group1_exam


def avg_custom_group(students, option, value):
    avg_custom_group_homework = 0
    avg_custom_group_exam = 0
    count_custom_group = 0
    for student in students:
        if student[option] == value or value == None:
            avg_homework_by_person, avg_exam_by_person = count_avg_by_person(student)
            avg_custom_group_homework += avg_homework_by_person
            avg_custom_group_exam += avg_exam_by_person
            count_custom_group += 1
    avg_custom_group_homework /= count_custom_group
    avg_custom_group_exam /= count_custom_group
    return avg_custom_group_homework, avg_custom_group_exam

def find_best(students):
    best_students = []
    all_students = []
    max_points = 0
    for student in students:
        homeworks, exam = count_avg_by_person(student)
        points = 0.6 * homeworks + 0.4 * exam
        if points > max_points:
            max_points = points
        all_students.append(points)
    for index, student_points in enumerate(all_students):
        if student_points == max_points:
            best_students.append(students[index]["Name"] +" "+ students[all_students.index(student_points)]["Surname"])
    print
    return best_students, max_points

def main():

    def input_option():
        option = input("Выберите параметр ([1]Пол, [2]Опыт программирования):")
        if option.upper() == "1":
            print("Средняя оценка за домашние задания у мужчин: {}\nСредняя оценка за экзамен у мужчин: {}\n\n\
Средняя оценка за домашние задания у женщин: {}\nСредняя оценка за экзамен у женщин: {}".format(*count_statistic(students, "Gender")))
        elif option.upper() == "2":
            print("Средняя оценка за домашние задания у студентов с опытом: {}\nСредняя оценка за экзамен у студентов с опытом: {}\n\n\
Средняя оценка за домашние задания у студентов без опыта: {}\nСредняя оценка за экзамен у студентов без опыта: {}".format(*count_statistic(students, "Experienced")))
        else:
            print("Неверная команда. Повторите ввод.")
            input_option()

    while True:
        comand = input("Введите команду ([1]Все студенты, [2]По признаку, [3]Лучшие студенты, [0]Закончить):")
        if comand.upper() == "1":
            print("Средняя оценка за домашние задания: {}\nСредняя оценка за экзамен: {}\n".format(*list(count_statistic(students,"Name"))))
        elif comand.upper() == "2":
            input_option()
        elif comand.upper() == "3":
            best_ones, max_points = find_best(students)
            if len(best_ones) > 1:
                print("Лучшие студенты: {0}. Максимальный балл: {1}".format(", ".join(best_ones), max_points))
            else:
                print("Лучший студент: {}. Максимальный балл: {}".format(best_ones[0], max_points ))
        elif comand.upper() == "0":
            print("Завершение работы. Нажмите любую клавишу")
            input()
            sys.exit()
        else:
            print("Неверная команда. Повторите ввод.")
            main()

if __name__ == '__main__':
    main()