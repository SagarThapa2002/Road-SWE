from calculator import run as calculator_app
from numberguess import play as number_guess_app
from todolist import manage as todo_list_app

def main():
    print("Welcome to Day-1 Projects")
    print("1. Calculator")
    print("2. Number Guessing Game")
    print("3. ToDo List Application")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator_app()
    elif choice == "2":
        number_guess_app()
    elif choice == "3":
        todo_list_app()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
