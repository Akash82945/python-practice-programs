import time
import os

os.system("cls" if os.name == 'nt' else 'clear')

# Uncomment these line to print normal stopwatch.
# print(" ===== Stop Watch Simulator =====")
# print("\nPress (Ctrl + C) to stop time...")

def stopwatch():
    try:              
        hours = 0
        minuets = 0
        second = 0
        total = (hours*3600) + (minuets*60) + second
        while True:
            print("\033[H",end=" ")     # Comment These 3 lines to print all time on terminal.
            print(" ===== Stop Watch Simulator =====")   # also this line
            print("\nPress (Ctrl + C) to stop time...")  # also this line

            mins,sec = divmod(total,60)
            hrs,mins = divmod(mins,60)
            stop_time = f"{hrs:02d} : {mins:02d} : {sec:02d}"
            time.sleep(1)
            total += 1
            print(stop_time)
            
            
    except KeyboardInterrupt:
        print(f"Your Taken Time : {total}")        

stopwatch()