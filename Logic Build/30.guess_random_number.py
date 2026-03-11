import random

computer = random.randint(1,100)
attempts = 0

print("Random Guessing Game.")

while True:
    user = int(input("Guess the number between 1 to 100: "))
    attempts += 1
    
    if user < computer:
        print("Try Higher number.")
    elif user > computer:
        print("Try Smallest number.")
    else:
        print(f"Correct! You tool {attempts} attempts.")
        print("Congurts 🎉")
        break