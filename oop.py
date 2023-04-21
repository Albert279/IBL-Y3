class Student:
    def __init__ (self, name, estate,course ):
        if not name():
            raise ValueError("please provide your name")
        if estate not in ["tena", "maxim","graceland"]:
            raise ValueError("Invalid estate")
        self.name = name
        self.estate = estate
        self.course = course
    def __str__ (self):
        return f"{self.name} is from {self.estate} and is persuing {self.course}"
def main ():
    student = get_student()
    print(student)
    
def get_student():
    name = input("your name? ").strip()
    estate = input ("your estate? ").strip()
    course = input("your course? ").strip()
    students= Student(name, estate, course)

if __name__ =="__main__":
    main()