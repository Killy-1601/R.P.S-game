import random

def guess_the_number():
    """Plays a 'Guess the Number' game."""
    secret_number = random.randint(1, 20)  # Computer chooses a number between 1 and 20
    attempts = 0

    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job! You guessed my number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
guess_the_number()