import random

choise = ["rock","paper","scissors"]

bot = random.choice(choise)

user = input("Enter your choice : ").lower()

if bot == user:
    print("Congurates")
else:
    print("Try Again!")

print(bot)