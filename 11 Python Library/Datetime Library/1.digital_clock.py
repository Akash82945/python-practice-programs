import datetime
import time
import os

try :
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        print("*"*30)
        print("  Digital Clock  ")
        print("*"*30)
        print(f" Time : {current_time}")
        print(f" Time : {current_time}", end="\r")
        print("*"*30)
        print("\nPress Ctrl + C to exit")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClock Stopped. Have a nice day!")