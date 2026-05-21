# import time
# import sys

# print("Task is progress... ")

# for i in range(15):
#     dots = "."*(i%4)
#     print(f"\rLoading{dots:<3}",end="")
#     time.sleep(0.5)
    
    
    

import time

frame = ['|','/','\\','-']

for i in range(20):
    
    spin = frame[i%len(frame)]
    
    print(f"\rLoading {spin}", end="")
    time.sleep(2)
    