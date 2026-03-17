def factorail(number):
   
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorail(number - 1)
    
print(factorail(5))
