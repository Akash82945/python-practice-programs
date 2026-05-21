# import time 
# import sys
# import os

# os.system("cls" if os.name == 'nt' else 'clear')

# message = "Hii, My Name is Akash Kumar."

# for word in message:
#     sys.stdout.write(word)
#     sys.stdout.flush()
#     time.sleep(0.5)



# import time
# message = "Hii, my name is Akash Kumar"
# words = message.split()
# for char in words:
#     print(f" {char}",end="")
    # time.sleep(0.5)
    
    


# import time
# import sys

# print("File downloding....")
# for i in range(5):
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(0.6)
    
    
    

import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

bol_na_halke  = [
    ("[Music Intro - Flute & Beats Playing...]", 21.0),
    ("Dhaage tod laao chaandni se noor ke", 12.0),          
    ("Ghoonghat hi bana lo roshni se noor ke", 13.0),       
    ("Dhaage tod laao chaandni se noor ke", 9.0),           
    ("Ghoonghat hi bana lo roshni se noor ke", 4.0),        
    ("Sharma gayi toh aaghosh mein lo", 3.0),               
    ("Ho saanson se uljhi rahein meri saansein", 4.0),      
    ("Bol na halke halke", 4.0),                            
    ("Bol na halke halke", 4.0),                            
    ("Honth se halke halke", 3.0),                          
    ("Bol na halke...", 7.0)                                
]



print("Bol Na Halke Song Lyrics. ===")
time.sleep(2) 

for line,delay in bol_na_halke:
    
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    
    time.sleep(delay)
    print()
    
print("Complete")





