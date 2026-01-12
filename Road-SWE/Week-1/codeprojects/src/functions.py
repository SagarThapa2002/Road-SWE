def Calculate_grade(percentage: float) -> str:
    if percentage >=70:
        return "Honoured by First Class."
    elif percentage >=60:
        return "Honoured by Second Class."
    elif percentage >=50:
        return "Honoured by Third Class."
    elif percentage >= 40:
        return "Pass"
    return "Fail."

class Student:
    def __init__(self, name: str, marks: list[float]):
        self.name= name
        self.marks = marks
    
    def percentage(self) -> float:
        return sum(self.marks)/len(self.marks)
    
    def grade(self) -> str:
        return Calculate_grade(self.percentage())

student = Student("Sagar",[85,95,65,98,87])
print(student.name)
print(student.percentage())
print(student.grade())
