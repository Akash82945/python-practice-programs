# Maximum number function
def maximum_number(number1, number2, number3):
    
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number3 and number2 > number1:
        return number2
    else:
        return number3
    
number1 = int(input("Enter number first: "))
number2 = int(input("Enter second first: "))
number3 = int(input("Enter third first: "))

result = maximum_number(number1,number2,number3)

print(result)