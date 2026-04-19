import random

computer = random.randint(1,100)
while True:
    user_input = int(input("Choose your no form 1 to 100 : "))
    if user_input > computer:
        print("Too High! Please Choose Lowest no.")
    elif user_input < computer:
        print("Too Low! Please Choose Highest no.")
    elif user_input == computer:
        print("Congurats. You Won!🎉")
        break
   