students = {}
while True:
    name = input('Введите имя студента (или `exit` для завершение:) ')
    if name == 'exit':
        break
    score = int(input('Введите оценку: '))
    students[name] = score

average_grade = sum(students.values()) // len(students)
highest_grade = max(students.values())
lowest_grade = min(students.values())

high_list = []
low_list = []
for student in students:
    if students[student] == highest_grade:
        high_list.append(student)
    if students[student] == lowest_grade:
        low_list.append(student)

print('Сводная информация по студентам: ')
for name, score in students.items():
    print(name+':', score)


print('\nCредний балл:',average_grade)
print('Наивысший балл:',highest_grade, ', '.join(high_list))
print('Наименьший балл:',lowest_grade, ', '.join(low_list))