class Student:

    def __init__(self, firstname, age, course, gender):
        self.firstname = firstname
        self.age = age
        self.course = course
        self.gender = gender

    def study(self):
        print(self.firstname, "is studying")

student1 = Student("John", 19, "Cybersecurity", "Male")
student1.study()

student2 = Student("Neema", 20, "Computer Science", "Female")
student2.study()

student3 = Student("Makena", 22, "Computer Science", "Male")