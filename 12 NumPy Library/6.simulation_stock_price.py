import numpy as np



# Task 6 : Simulate stock price

def stock_price():
    start_price = 500
    days = int(input("Enter Number of days : "))
    np.random.seed(42)

    # daily_changes = np.random.normal(loc=0, scale=1.5, size=days)
    daily_changes_in_percent = np.random.normal(loc=0.0005, scale=0.015, size=days)
    
    # stock_movements = np.cumsum(daily_changes)
    stock_movements = np.cumsum(daily_changes_in_percent)
    
    stock_price = start_price + stock_movements
    stock_price = start_price*np.exp(np.cumsum(daily_changes_in_percent))

    for price,changes in zip(stock_price,daily_changes_in_percent):
        print(f"Day {days} : ${price:.2f} : ({changes:.2f})")
        days += 1
        
stock_price()