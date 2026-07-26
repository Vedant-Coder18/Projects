import random

print("                           wlecome to Rock,Paper and Scissors Game                        \n")

a=["rock",'paper','Scissors']

b=random.choice(a)
c=input("Enter your choice- Rock\Paper\Scissors --\n").lower()

if b==c:
    print("Draw.....\n" 
    "try again")

elif b=="rock" and c=="paper":
    print("You Won...\n" 
    "congrats")

elif b=="paper" and c=="rock":
    print("You Lost...\n"
    "try again")

elif b=="scissors" and c=="paper":
    print("You Lost...\n" 
    "try again")

elif b=="paper" and c=="scissors":
    print("You Won...\n" 
    "congrats") 

elif b=="scissors" and c=="rock":
    print("You Won...\n" 
    "congrats")

elif b=="rock" and c=="scissors":
    print("You lost...\n" 
    "try again")

print("The computer's choice was -",b)