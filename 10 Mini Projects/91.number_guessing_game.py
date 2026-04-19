# import random

# computer = random.randint(1,100)

# count = 6

# while True:
#     user_input = int(input("Choose your no form 1 to 100 : "))
#     count -= 1
    
#     if user_input > computer:
#         print("Too High! Please Choose Lowest no.")
#     elif user_input < computer:
#         print("Too Low! Please Choose Highest no.")
#     elif user_input == computer:
#         print("Congurats. You Won!🎉")
#         break
   
   
   
import random

def number_guessing_game():
    
    print("===== Random Number Guessing Game. =====")
    
    computer = random.randint(1,100)
    
    attempts = 7
    score = 0
    
    print(f"You have {attempts} Attempts to Guess correct Number.")
    
    for i in range(1,attempts+1):
        guess = int(input(f"Guess no {i} - Between(1-100) :"))
        if guess > computer:
            print("Too High! Please Guees lowest no.")
        elif guess < computer:
            print("Too Low! Please Guess highest no.")
        elif guess == computer:
            print("You Won! Congratulations🎉")
            score = (attempts - i + 1)*10
            break
        else:
            print("Invalid Guess.")
    if score == 0:
        print(f"Out of attempts! Correct no is {computer}")
            
while True:
    number_guessing_game()
    user_input = input("Do you want to play again. (y/n): ").lower()
    if user_input == 'y':
        print("Thanks Visit Again.👋")
    break