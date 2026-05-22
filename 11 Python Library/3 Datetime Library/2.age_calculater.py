# Age Calculater Simulater
import datetime
import calendar

print(" ===== Age Calculator =====")

birth_year = int(input("Enter Birth Year (eg. 2004) : "))
birth_month = int(input("Enter Birth Month (eg. 1-12) : "))
birth_day = int(input("Enter Birth Day (eg. 1-31) : "))


birth_date = datetime.date(birth_year,birth_month,birth_day)
today = datetime.date.today()

if birth_date > today:
    print("Error! Birthday date.")

else:
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        
        prev_month = today.month -1 if today.month >1 else 12
        prev_year = today.year if today.month > 1 else today.year -1
        
        if prev_month in [4,6,9,11]:
            days += 30
        elif prev_month == 2:
            if (prev_year % 4 == 0 and prev_year % 100 != 0 ) or (prev_year % 400 == 0):
                days += 29
            else:
                days += 28
        else:
            days += 31
            
            months -= 1
        
    if months < 0:
        months += 12
        years -= 1
            


    #total days
    total_days = (today - birth_date).days
    rem_month_day = days
    total_months = (years*12) + months
    total_weeks = (total_days // 7) 
    rem_days = (total_days % 7)
    total_hours = total_days * 24
    total_min = total_hours * 60
    total_sec = total_min * 60




    print("*"*30)
    print(" === Age Calculater =====")
    print("*"*30)
    print("Age: \n")
    print(f"{years} Years {months} Months {days} Days")
    print(f"or {total_days} Days ")
    print(f"or {total_months} Months {rem_month_day} Days")
    print(f"or {total_weeks} Weeks {rem_days} Days")
    print(f"or {total_hours} Hours")
    print(f"or {total_min} Minutes")
    print(f"or {total_sec} Seconds")


    calendar.setfirstweekday(calendar.SUNDAY)
    years = birth_year
    months = birth_month

    today_year = today.year
    today_month = today.month

    months_calendar = calendar.month(years,months)
    today_calendar = calendar.month(today_year,today_month)
    print("\nBirth Month Calendar.\n",months_calendar)
    print("\nToday Month Calendar.\n",today_calendar)
