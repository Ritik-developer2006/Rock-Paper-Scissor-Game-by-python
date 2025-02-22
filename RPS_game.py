import random
print("Rules are :- \n 1 => Rock \n 2 => Paper \n 3 => Scissor")

# take input from user
number = input("Please Enter a number according to your choice : ")

# Validate input
if number not in ["1", "2", "3"]:
    print("Invalid input! Please enter a number between 1 and 3.")
    exit()

# Map input to the corresponding choice
value = ["rock", "paper", "scissor"][int(number) - 1]
print("You selected:", value)

# Generate computer's choice
computer_choice = random.randint(1, 3)
computer_value = ["rock", "paper", "scissor"][computer_choice - 1]
print("Computer selected:", computer_value)

# Determine the winner
if number == str(computer_choice):
    print("It's a draw! Try again!")
elif (number == "1" and computer_choice == 3) or (number == "2" and computer_choice == 1) or (number == "3" and computer_choice == 2):
    print("You won!")
else:
    print("You lost!")
