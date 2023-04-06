students = ["kevin", "sheldon", "brian", "jonte", "caro"]
estates = ["kasarani", "westie", "roysambu", "kayole", "exit9"]

students = {
    "kevin":"kasarani",
    "sheldon":"westie",
    "brian":"roysambu",
    "jonte":"kayole",
    "caro":"exit9"  
} 

print(students["jonte"])

for student in students:
    print(student, students[student], sep="...")