
# List
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Set
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)
list_students.sort()
students_grades = {list_students[0] : sum(grades[0]) / len(grades[0])}
for i in range(0, len(list_students)):
    students_grades[list_students[i]] = {sum(grades[i]) / len(grades[i])}
# students_grades = {list_students[0] : sum(grades[0]) / len(grades[0])}
# students_grades[list_students[1]] = {sum(grades[1]) / len(grades[1])}
# students_grades[list_students[2]] = {sum(grades[2]) / len(grades[2])}
# students_grades[list_students[3]] = {sum(grades[3]) / len(grades[3])}
# students_grades[list_students[4]] = {sum(grades[4]) / len(grades[4])}
print("Average score of students:", students_grades)