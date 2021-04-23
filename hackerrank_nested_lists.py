n = int(input("Nr of students: "))
list_nest = []
list_grades = []


def creating_catalog():

    for i in range(n):
        name = input("Student name: ")
        score = float(input("Grade: "))
        list_nest2 = [name, score]
        list_grades.append(score)
        list_nest.append(list_nest2)
    return list_nest


def ordering_students(list_students):
    list_grades.sort()
    result = []
    sorted_list = []
    for i in list_students:
        if i[1] == list_grades[1]:
            result.append(i[0])
        sorted_list = sorted(result, key=str.lower)
    return sorted_list


creating_catalog()
print(ordering_students(list_nest))
