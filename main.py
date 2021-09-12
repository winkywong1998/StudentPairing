import Student
import Group

student1 = Student.Student("Anna", "123", "CS", "2", "0", True, 1)
student2 = Student.Student("Bob", "456", "BME", "1", "0", False, 2)
student3 = Student.Student("Charlie", "789", "AMS", "3", "0", True, 1)

student_list = [student1, student2, student3]
group = Group.Group(student_list)

print(student3)
print(group.major)
print(group.purpose)
print(group.pref)
