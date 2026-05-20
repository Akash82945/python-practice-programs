import time
import os

os.system("cls" if os.name == 'nt' else 'clear')

def get_time():
    
    while True:
        try:
            
            time_input = input("Enter Time Format -> HH:MM:SS or MM:SS :- ")
            
            parts = list(map(int, time_input.split(':')))
            
            if len(parts) == 3:
                h,m,s = parts
            
            elif len(parts) == 2:
                h,m,s = 0 , parts[0] , parts[1]
            
            elif len(parts) == 1:
                h,m,s = 0,0, parts[0]
            else:
                print("Invalid Time format.")
                continue
            
            return (h*3600) + (m*60) + s
        
        except ValueError:
            print("Invalid Error.")

total = get_time()


min,sec = divmod(total,60)
hrs,min = divmod(min,60)
formatd_time = f"{hrs:02d} : {min:02d} : {sec:02d}"
print(f"\nYour Set Time is ({formatd_time})")
print("-"*30)
print("===== Count Down Programs =====")
print("-"*30)

while total >= 0:
    # print("\033[H", end=" ")
    
    min,sec = divmod(total,60)
    hrs,min = divmod(min,60)
    formated_time = f"{hrs:02d} : {min:02d} : {sec:02d}"
    print(f"Remainig Time -> {formated_time}")
    time.sleep(1)
    total -= 1
    
print("Time Up!")