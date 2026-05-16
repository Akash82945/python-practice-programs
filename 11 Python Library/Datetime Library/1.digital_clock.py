import datetime
import time
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

try :
    while True:
        print("\033[H", end="")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        print("*"*30)
        print("  Digital Clock  ")
        print("*"*30)
        print(f" Time : {current_time}")
        print("*"*30)
        print("\nPress Ctrl + C to exit")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClock Stopped. Have a nice day!")