import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the number guessing game")
    print(f"I am thinking of a number between 1 and 100. You have to guess{max_attempts} to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter the number:"))
        except ValueError:
            print("Invalid input!Please enter the value")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again")
        elif guess > secret_number:
            print("Too high! Try again")
        else:
            print(f"Congraculations! you guessed it correct in {attempts} attempts")
            break

        if attempts >= max_attempts:
            print(f"Sorry you ran out of attempts. The number was {secret_number}")

number_guessing_game()