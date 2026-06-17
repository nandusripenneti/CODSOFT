import random

user = input("Enter rock, paper or scissors: ")

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("Tie")

elif user == "rock" and computer == "scissors":
    print("You Win")

elif user == "paper" and computer == "rock":
    print("You Win")

elif user == "scissors" and computer == "paper":
    print("You Win")

else:
    print("You Lose")
