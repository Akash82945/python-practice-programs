import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

current_time = time.strftime("%H:%M:%S")
print(f"Current Time : {current_time}")


# target = '01:45:00'
target = input("Select Time Schedule (format ->  HH:MM:SS) : ")
target_time = time.strptime(target,"%H:%M:%S")
readable_time = time.strftime("%H:%M:%S",target_time)
print(f"Target Time : {readable_time}")

# message = "Hii, I am Akash Kumar."
message = input("Enter Your message : ")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\033[H",end=" ")

    current_time = time.strftime("%H:%M:%S")
    print("-"*40)
    print(" ===== Delayed Message App ===== ")    
    print("-"*40)
    print(f"Target Time : {readable_time}")
    print(f"Current Time : {current_time}")
    print(f"Your Message : {message}")

    if current_time >= readable_time:
        print(message)
        print("Message Sent.")
        break
    else:
        time.sleep(1)
        
    
    