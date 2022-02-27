classroom = []

for i in range(7):
    classroom.append([])
    for students in range(1,11,2):
        classroom[i].append(students)

print(classroom)


# for students in range(1,11):
#     print(students, end= " ")