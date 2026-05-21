# import time
# import sys

# print("Task is progress... ")

# for i in range(15):
#     dots = "."*(i%4)
#     print(f"\rLoading{dots:<3}",end="")
#     time.sleep(0.5)
    
    
    

# import time
# frame = ['|','/','\\','-']
# for i in range(20):
#     spin = frame[i%len(frame)]
#     print(f"\rLoading {spin}", end="")
#     time.sleep(0.2)
    
    
    

import time
import sys
import threading

print("We Count number from (1-100000000)")
def background_task():
    start = time.time()
    count = 0
    for i in range(0,100000000):
        count += 1
    end = time.time()
    print(end - start)
    # time.sleep(3)

task_thread = threading.Thread(target=background_task)
task_thread.start()

spinner = ['|','\\','-','/']
idx = 0

while task_thread.is_alive():
    print(f"\rWorking... {spinner[idx%len(spinner)]}",end="")
    idx += 1
    time.sleep(0.1)
    
print("\rProcess is Complete")