import random

user_choice=input("what is your choice?(rock,paper,scissors):")
list=["rock","paper","scissors"]
com_choice=random.choice(list)

if user_choice==com_choice:
    print("try again")
elif user_choice=="rock":
    if com_choice=="scissors":
        print("rock smashes scissors! you win!!")
    else:
        print("paper covers rock! you lose.")
elif user_choice=="paper":
    if com_choice=="rock":
        print("paper covers rock! you win!!")
    else:
        print("scissors cuts paper! you lose.")
elif user_choice=="scissors":
    if com_choice=="paper":
        print("scissors cuts paper! you win!!")
    else:
        print("rock smashes scissors! you lose.")