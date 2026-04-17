num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print(f"{num1} is smallest than {num2}, {num3}.")
    
elif num2 < num3 and num2 < num1:
    print(f"{num2} is smallest than {num1}, {num3}.")
   
else:
    print(f"{num3} is samllest than {num1}, {num2}.")