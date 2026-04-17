num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 > num3:
    print(f"{num1} is Largest then {num2} , {num3}.")
    
elif num2 > num3 > num1:
    print(f"{num2} is Largest then {num1} ,{num3}.")
    
else:
    print(f"{num3} is Largest then {num1} , {num2}.")