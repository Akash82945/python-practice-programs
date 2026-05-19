import time
import os
import sys
import datetime
from playsound import playsound  #type: ignore


# Delay program
# print('Start')
# time.sleep(3)
# print('End')



# Timer
# start = time.time()
# count = 0
# for i in range(1,1000):
#     count += 1
# print("Python")
# end = time.time()
# print(end - start)


# Count time for user input
# start = time.time()
# user_input = input("Enter your name : ")
# end = time.time()
# print('Your name : ',user_input)
# print("Time taken : ", end - start)



# Digital clock
# os.system('cls' if os.name == 'nt' else 'clear')
# try :
#     while True:
#         print("\033[H", end="")
#         print(" ===== Digital Clock =====\n")
#         digital_time = time.strftime("%H:%M:%S")
#         print("Time :  ",digital_time)
#         second = time.sleep(1)
# except KeyboardInterrupt:
#     print("\nClock off.")




# Reverse Timer
# import time
# import os
# import sys
# from playsound import playsound  #type: ignore

# def get_time():
#     try:
#         while True:
#             try:
#                 user_input = input("Enter Time format -> HH:MM:SS or MM:SS or SS : ")
                
#                 parts = list(map(int, user_input.split(":")))
                
#                 if len(parts) == 3:
#                     h,m,s = parts
#                 elif len(parts) == 2:
#                     h,m,s = 0, parts[0],parts[1]
#                 elif len(parts) == 1:
#                     h,m,s = 0,0,parts[0]
#                 else:
#                     print("Invalid time format.")
#                     continue
#                 if m >= 60 or s >= 60 or h < 0 or m < 0 or s < 0:
#                     print("Also invlid time.")
#                     continue
#                 return (h*3600)+(m*60)+s
        
#             except ValueError:
#                 print("Invalid Inputs")
    
#     except KeyboardInterrupt:
#         print("Stopped by user.")
#         sys.exit()
        
# total = get_time()
# os.system('cls' if os.name == 'nt' else 'clear')

# print(" ===== Countdown Timer =====") 
# min,sec = divmod(total, 60)
# hrs,min = divmod(min,60)
# time_set = f"{hrs:02d} : {min:02d} : {sec:02d}"

# print("-"*30)
# print(f"You Set Time ({time_set})")
# print("-"*30)

# try:
#     while total >= 0:
#         min,sec = divmod(total, 60)
#         hrs,min = divmod(min,60)
#         time_set = f"{hrs:02d} : {min:02d} : {sec:02d}"
#         print('Time left : ',time_set, " ")
#         total -= 1
#         time.sleep(1)

#     print("Time's Up!")
#     print("Timer alert....")
#     playsound("faaah.mp3")
    
# except KeyboardInterrupt:
#     print("Timer Stopped by user.")





# Time Zone converter
local_time = time.strftime("%H:%M:%S")
date = time.strftime("%d-%b-%Y")
print(f"PC local Time : {local_time}")
print(f"Date : {date}")
global_time = time.gmtime()
format_global_time = time.strftime("%H:%M:%S",global_time)
format_global_date = time.strftime("%d-%m-%Y",global_time)
print("Global UTC Time : ", format_global_time)
print("Global UTC Date : ", format_global_date)

india_time = datetime.datetime.now()
global_utc_time = datetime.datetime.utcnow()
time_diff = india_time - global_utc_time
print('Time Different Global to Local Time : ',time_diff)





# Advance: Convert string time to real time
# string_time = "25-12-2026 18:30:00"
# real_time1 = "%d-%m-%Y %H:%M:%S"
# real_time = time.strptime(string_time,real_time1)
# format_time = time.strftime("%H:%M:%S",real_time)
# format_date = time.strftime("%d-%m-%Y",real_time)
# print(format_time)
# print(format_date)