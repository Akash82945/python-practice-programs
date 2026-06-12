import numpy as np



# Task 6 : Simulate stock price

def stock_price():
    start_price = 500
    days = int(input("Enter Number of days : "))
    np.random.seed(42)

    daily_changes = np.random.normal(loc=0, scale=1.5, size=days)
    stock_movements = np.cumsum(daily_changes)
    stock_price = start_price + stock_movements

    # print(f"Day 1 : ${stock_price[0]:.2f} (changes {daily_changes[0]:.2f})")
    for price,changes in zip(stock_price,daily_changes):
        print(f"Day {days} : ${price:.2f} : ({changes:.2f})")
        days += 1
        
stock_price()