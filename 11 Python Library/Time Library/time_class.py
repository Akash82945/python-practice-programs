import time
import os


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

input_hour = int(input("Enter timer Hours : "))
input_min = int(input("Enter minutes : "))
input_sec = int(input("Enter second : "))

total = (input_hour * 3600) + (input_min * 60) + input_sec
os.system('cls' if os.name == 'nt' else 'clear')

min,sec = divmod(input_sec, 60)
hrs,min = divmod(min,60)
time_set = f"{hrs:02d} : {min:02d} : {sec:02d}"
print(f"You Set Time : {time_set}")
    
while total >= 0:
    print(total)
    total -= 1
    time.sleep(1)

    
    