import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'sisr']
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'sisr'. Type 'exit' to quit.")

    while True:
        user_choice = input("👉 Your choice: ").lower()
        if user_choice == 'exit':
            print("👋 Thanks for playing!")
            break
        if user_choice not in choices:
            print("⚠️ Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"💻 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'sisr') or
            (user_choice == 'sisr' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

# Run the game
rock_paper_scissors()
