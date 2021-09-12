import Student
import Group

student1 = Student.Student("a", "123", "0", "2", "dasd")
student2 = Student.Student("b", "456", "1", "1", "dasd")
student3 = Student.Student("c", "789", "2", "3", "dasd")

student_list = [student1, student2, student3]
group = Group.Group(student_list)

print(group.major)
print(group.purpose)
print(group.pref)


