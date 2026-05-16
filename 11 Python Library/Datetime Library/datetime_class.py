# Current date and time
# import datetime
# now = datetime.datetime.now()
# print(now)


# Current date
# import datetime
# today = datetime.date.today()
# print(today)


# Current time
import datetime
# current_time = datetime.datetime.now().time()
# current_time = datetime.datetime.now().time().replace(microsecond=0)
# print(current_time)
current_time = datetime.datetime.now()
formate_time = current_time.strftime("%H:%M:%S")
print(formate_time)