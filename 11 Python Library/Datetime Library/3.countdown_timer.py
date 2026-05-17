import datetime
import os
import time
from playsound import playsound  # type: ignore

os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 35)
print("       SETUP COUNTDOWN TIMER       ")
print("=" * 35)

try:
    target_hr = int(input("Set hours : "))
    target_min = int(input("Set minutes : "))
    target_sec = int(input("Set second : "))

    total_sec = (target_hr * 3600) + (target_min * 60) + (target_sec)
    set_time_format = f"{target_hr:02d} : {target_min:02d} : {target_sec:02d}"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    print(f"\n === Timer Started (Set Time : {set_time_format})===\n")        
        
    while total_sec >= 0:
        # print("\033[H", end="")
        
        min,sec = divmod(total_sec,60)
        hrs,min = divmod(min,60)
        
        timer_format = f"{hrs:02d}:{min:02d}:{sec:02d}"
        
        print(f"Time Remaining : {timer_format}", end="\r")
        
        time.sleep(1)
        total_sec -= 1
        
    print("\n\n" + '*'*30)
    print("Times up! Countdown Finished")
    print ('*'*30)
    
    print("Playing alarm music...")
    playsound("faaah.mp3")
        
        
except ValueError:
    print("\nError! please enter valid time")