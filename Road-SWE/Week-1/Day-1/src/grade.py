#Grading system using python
def calculate_grade():
        print("/n Please enter your marks of following module to know your grade:")
        m1=float(input("Linear Algebra and Calculus: "))
        m2=float(input("Advanced Aritificial Intelligence: "))
        m3=float(input("Networking and Computer Systems: "))
        m4=float(input("Database Management Systems: "))
        m5=float(input("Software Engineering: "))
        total_marks= m1 + m2 + m3 + m4 + m5
        marks= (total_marks/500)*100
        print(f"Your total marks are: {total_marks} out of 500")
        print(f"Your percentage is: {marks}%")
    
        if marks >= 70:
            print("Excellent! You have honored with First Class.")
        elif marks >=60 and marks <70:
            print("Good! You have honored with Second Class.")
        elif marks >=50 and marks <60:
            print("You have honored with Third Class.") 
        elif marks >=40 and marks <50:
            print("You have passed the exam with a Pass Class.")
        else:
            print("Unfortunately, you have failed the exam. Better luck next time!")
def grade():
    while True:
        print("Here is the Results of the Grading System:")
        exit = input("Do you want to continue? (yes/no): ")
        if exit.lower() == 'no':
            print("Exiting Grading System. Goodbye!")
            break
        elif exit.lower() == 'yes':
            calculate_grade()

    