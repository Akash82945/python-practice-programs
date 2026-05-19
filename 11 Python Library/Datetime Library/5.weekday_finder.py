import datetime

time = datetime.datetime.now().replace(microsecond=0)

weekday = time.strftime("%a")
full_weekday = time.strftime("%A")
print("Short name of week day :",weekday)
print('Full name of week day : ',full_weekday)