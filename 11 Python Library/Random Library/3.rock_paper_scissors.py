import random

count = 0
print("===== Welcome to Rock Paper Scissor Game =====")
while True: 
    choise = ["rock","paper","scissors",'r','p','s']

    bot = random.choice(choise)

    user = input("Enter your choice [r/p/s]: ").lower()

    if bot == user:
        count += 1
        print("Congurates. You Win.🎉")
        print(f"You win this gane {count} times.")
    else:
        print("Try Again!🔁")

    if user == 'q':
        break