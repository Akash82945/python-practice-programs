import random

def dice_rolling():
    
    dice = random.randint(1,6)
    
    if dice == 1:
        print(f'''
              +-----+
              |     |
              |  1  |
              |     |
              +-----+
              ''')
    
    elif dice == 2:
        print(f'''
              +-----+
              |     |
              |  2  |
              |     |
              +-----+
              ''')
        
    elif dice == 3:
        print(f'''
              +-----+
              |     |
              |  3  |
              |     |
              +-----+
              ''')
        
    elif dice == 4:
        print(f'''
              +-----+
              |     |
              |  4  |
              |     |
              +-----+
              ''')
        
    elif dice == 5:
        print(f'''
              +-----+
              |     |
              |  5  |
              |     |
              +-----+
              ''')
        
    elif dice == 6:
        print(f'''
              +-----+
              |     |
              |  6  |
              |     |
              +-----+
              ''')
    
dice_rolling()