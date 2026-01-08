# Number Guessing Game using Python
import random
def play():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = input("Enter your guess (or type 'exit' to quit): ")
        if user_guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break

        try:
            user_guess = int(user_guess)
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")