# Lottery number generator
import random


def lottery_number():
    
    lucky_number = random.sample(range(1,49),6)
    lucky_number.sort()
    return lucky_number
    
print(lottery_number())