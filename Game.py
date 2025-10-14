import random

def number_guessing_game():
    # Computer ek random number lega
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
            break

number_guessing_game()
