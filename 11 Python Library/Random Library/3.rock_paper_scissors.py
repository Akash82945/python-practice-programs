import random

count = 0
print("===== Welcome to Rock Paper Scissor Game =====")
map = {'r':'rock','rock':'rock','Rock':'rock',
           'p':'paper','Paper':'paper','paper':'paper',
           's':'scissor','scissor':'scissor','Scissor':'scissor'}
while True: 

    choise = ['rock','paper','scissor']
    bot = random.choice(choise)

    user_input = input("\nEnter your choice [r/p/s] or 'q' for quit: ").lower()
    
    if user_input == 'q':
        print("Thanks for playing! Bye.👋")
        break
    
    if user_input not in map:
        print("Invalid Choise!")
        continue
    
    user = map[user_input]
    print(f"You Choose '{user}'")
    print(f"Bot choose '{bot}'")

    if bot == user:
        print("Game draw!🤝")
    elif (user == "rock" and bot == "scissor") or\
        (user == "scissor" and bot == "paper") or\
            (user == "paper" and bot == "rock"): 
        count += 1
        print("Congurates. You Win.🎉")
        print(f"You win this gane {count} times.")
    else:
        print("Try Again!🔁 Bot Win.🤖")
