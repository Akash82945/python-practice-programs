import datetime

time = datetime.datetime.now().replace(microsecond=0)

weekday = time.strftime("%a")
full_weekday = time.strftime("%A")
print("Short name of week day :",weekday)
print('Full name of week day : ',full_weekday)


weekday = time.weekday()          # weekday() start 0 from monday
weekday2 = time.isoweekday()      # isoweekday() start 1 from monday
print(weekday)
print(weekday2)


# isocalander is use for finding year , week , day
# calendar = time.isocalendar()
# print(calendar)


if time.weekday() >= 5:
    print("Yay! Its weekend holiday.")
else:
    print("Sorry!, Today weekday.")