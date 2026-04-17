# Function of finding the factorial of given number.
def factorail(number):
   
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorail(number - 1)
    
# print(factorail(5))

number = int(input("Enter the number: "))
result = factorail(number)
print(f"{result} is factorial of {number}")