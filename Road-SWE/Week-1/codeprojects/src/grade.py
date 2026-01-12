from typing import List

def calculate_percentage(marks: List[float]) -> float:
    total_marks=sum(marks)
    return (total_marks/500)*100

def determine_grade(percentage: float) -> str:
    if percentage >=70:
        return "First Class."
    elif percentage >=60:
        return "Second Class."
    elif percentage >=50:
        return "Third Class."
    elif percentage >=40:
        return "Pass Class."
    else:
        return "Fail."