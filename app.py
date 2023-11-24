import random

print("Welcome to my Rock-Paper-Scissors game...")

while True:
    choice = input("Please choose either 'rock', 'paper', or 'scissors': ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        print("You chose: ", choice)
    else:
        print("Invalid input! You haven't entered rock, paper or scissors, try again.")
        continue

    computer = random.choice(['rock', 'paper', 'scissors']).lower()
    print("The computer chose: ", computer)

    if choice == computer:
        print("It's a tie!")
    elif (choice == 'rock' and computer == 'scissors') or (choice == 'paper' and computer == 'rock') or (choice == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break