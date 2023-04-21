class First_name:
    def ___init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        
        
        
class Student(First_name):
    def __init__(self, name,course):
        super().__init__(name)
        self.course = course

class Teacher(First_name):
    def __init__(self, name,units):
        super().__init__(name)
        self.units = units   
def __str__(self):
        return f"{self.name} is is teaching {self.units}"

def main():
    student = Student("Bostone", "Information Science")
    teacher = Teacher("Ochieng", "Python Programming")
    print(student)
    print(teacher)

if __name__ == "__main__":
    main()
