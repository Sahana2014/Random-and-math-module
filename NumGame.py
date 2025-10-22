import random
playing = True
number = str(random.randint(10, 20))

print("Welcome to the Math Operators Game!")
print("I have selected a number between 10 and 20.")
print("Try to guess the number")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if guess == number:
        print("Congratulations! You've guessed the correct number! You win!")
        print("The number was:", number)
        break
    
    else:
        print("Incorrect guess. Try again!")