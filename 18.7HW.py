import random
from types import new_class

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Редактирование ученика
        5. Редактирование предмета
        6. Редактирование оценки
        7. Удаление ученика
        8. Удаление предмета
        9. Удаление оценки
        10. Вывод всех оценок для определенного ученика
        11. Вывод среднего балла по каждому предмету для определенного ученика
        12. Добавление нового предмета
        13. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Редактирование ученика')
        student = input('Введите имя ученика: ')
        newstudent = input('Введите новое имя ученика: ')
        if student in students_marks.keys():
            students_marks[newstudent] = students_marks[student]
            del students_marks[student]
            print (f'Имя {student} изменено на {newstudent}')
            print(f'''{student}
                    {students_marks[newstudent]}''')
        else:
            print('Неверное имя ученика')
    elif command == 5:
        print('5. Редактирование предмета')
        class_ = input('Введите название предмета: ')
        classNew = input('Введите новое название предмета: ')
        if class_ in students_marks[student]:
            del students_marks[student][class_]
            students_marks.update({class_:classNew})
            print (f'Предмет {class_} изменен на {classNew}')
        else:
            print('Неверное название предмета')
    elif command == 6:
        print('6. Редактирование оценки')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Все оценки по предмету {class_}:{students_marks[student][class_]}')
            n = int(input('Введите индекс редактируемой оценки: '))
            if 0 <= n < len (students_marks[student][class_]):
                n1 = int(input('Введите новую оценку: '))
                students_marks[student][class_][n] = [n1]
                print(f'Оценка изменена, обновленный список оценок: {students_marks[student][class_]}')
            else:
                print('Неверно введен индекс оценки.')
        else:
            print('Неверно введено имя ученика, или название предмета')
    elif command == 7:
        print('7. Удаление ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            students.remove(student)
            del students_marks[student]
            print(f'Ученик удален, обновленный список учеников: {students}')
        else:
            print('Неверно введено имя ученика')
    elif command == 8:
        print('8. Удаление предмета')
        name = input('Введите название предмета: ')
        if student in students_marks.keys():
            classes.remove(name)
            del students_marks[student][name]
            print(f'Предмет удален, обновленный список предметов: {classes}')
        else:
            print('Неверно введено название предмета')
    elif command == 9:
        print('9. Удаление оценки')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        mark = int(input('Введите индекс оценки для удаления: '))
        if mark in students_marks[student][class_]:
            del students_marks[student][class_][mark]
            print(f'Оценка удалена, обновленный список оценок: {students_marks[student][class_]}')
        else:
            print('Неверно введен индекс оценки')
    elif command == 10:
        print('10. Вывод всех оценок для определенного ученика')
        student = input('Введите имя ученика: ')
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 11:
        print('11. Вывод среднего балла по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for classes,marks in students_marks[student].items():
                marks_sum = sum(marks)
                marks_count = len(marks)
                print(f'{classes} - {marks_sum//marks_count}')
        else:
            print('Неверное имя ученика')
    elif command == 12:
        print('12. Добавление нового предмета')
        new_class = input('Введите название нового предмета: ')
        classes.append(new_class)
        for student in students_marks:
            students_marks[student][new_class] = []
            print(f'Предмет {new_class} успешно добавлен.')
    elif command == 13:
        print('13. Выход из программы')
        break
