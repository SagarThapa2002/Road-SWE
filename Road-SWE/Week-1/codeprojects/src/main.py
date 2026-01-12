# src/main.py

from calculator import run as calculator_app
from numberguess import play as number_guess_app
from todolist import manage as todo_list_app
from grade import calculate_percentage, determine_grade
from tax_calculator import IncomeTaxCalculator  


def get_marks() -> list[float]:
    """Get validated marks for grading system"""
    print("\nPlease enter your marks:")
    subjects = [
        "Linear Algebra and Calculus",
        "Advanced Artificial Intelligence",
        "Computer Systems and Networking",
        "Database Management Systems",
        "Software Engineering"
    ]
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if mark < 0 or mark > 100:
                    raise ValueError("Marks must be 0-100")
                marks.append(mark)
                break
            except ValueError as e:
                print("Invalid input:", e)
    return marks


def run_tax_calculator() -> None:
    """Run UK Income Tax Calculator"""
    try:
        gross_income = float(input("\nEnter your gross income (£): "))
        if gross_income < 0:
            raise ValueError("Income cannot be negative.")

        calculator = IncomeTaxCalculator(gross_income)

        print("\n--- UK Income Tax Summary (2024/2025) ---")
        print(f"Gross income: £{gross_income:,.2f}")
        print(f"Taxable income: £{calculator.taxable_income():,.2f}")
        print(f"Tax rate: {calculator.tax_rate() * 100:.0f}%")
        print(f"Tax due: £{calculator.tax_due():,.2f}")

    except ValueError as error:
        print(f"Invalid input: {error}")


def main() -> None:
    """Menu-driven entry point for all apps"""
    while True:
        print("\n--- STUDENT & UTILITY APPS MENU ---")
        print("1. Simple Calculator")
        print("2. Number Guessing Game")
        print("3. To-Do List Manager")
        print("4. Grading System")
        print("5. UK Income Tax Calculator")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            calculator_app()
        elif choice == "2":
            number_guess_app()
        elif choice == "3":
            todo_list_app()
        elif choice == "4":
            marks = get_marks()
            percentage = calculate_percentage(marks)
            grade = determine_grade(percentage)
            print("\n--- Result Summary ---")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Grade: {grade}")
        elif choice == "5":
            run_tax_calculator()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option, please select 1-6.")


if __name__ == "__main__":
    main()
