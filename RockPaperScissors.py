import random

options = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ")

computer_choice = random.choice(options)

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors"):
    print("You win! Rock crushes scissors.")
elif (user_choice == "paper" and computer_choice == "rock"):
    print("You win! Paper covers rock.")
elif (user_choice == "scissors" and computer_choice == "paper"):
    print("You win! Scissors cut paper.")
else:
    print("You lose! Better luck next time.")