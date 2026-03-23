# Simple OOPS Example using Student

class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("New student created")

    # Method to show details
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
student1 = Student("Riya", 10)
student2 = Student("Aman", 11)

# Calling methods
student1.show_details()
print("-----")
student2.show_details()
