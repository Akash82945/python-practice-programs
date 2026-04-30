# Dice Rolling Mini Project
import random

def dice_rolling():
    
    while True:
        
        rolling = input("Press 'enter' to Rollin and 'q' for quit :" ).lower()
        
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
                
            
        if rolling == 'Q'.lower():
            print("Good Bye!")
            break
    
# dice_rolling()

if __name__ == '__main__':
    dice_rolling()