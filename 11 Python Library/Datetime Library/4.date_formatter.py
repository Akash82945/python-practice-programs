import datetime
# import time

time = datetime.datetime.now().replace(microsecond=0)

print(f"Default time : {time}")

formatter_time = time.strftime("%H:%M:%S:%p")
print("Formatted Time : ",formatter_time)

day = time.strftime("%A")
print("Today Day : ",day)

formatted_date = time.strftime("%d-%B-%Y")
formatted_date2 = time.strftime("%d-%m-%y")
print("Formatted Date in digit : ",formatted_date2)
print("Formatted Date : ",formatted_date)

