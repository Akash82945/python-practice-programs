# Finding pi value using Math Library
# import math
# pi_vlaue = math.pi
# print(pi_vlaue)


# Finding Factorial
# import math
# fact = math.factorial(5)
# print(fact)


# finding square root
# import math
# sq_root = math.sqrt(25)
# print(sq_root)


# # Printing the all functions of math library
# import math
# fun = dir(math)
# print(fun)


print("In this File there are 5 Assignmet Question.")

import math

def area_circle():
    r_value = float(input("Enter the value of r :"))
    result = math.pi*(r_value*r_value)
    return f"Area of circle is {result}"

def square_root():
    user_input = int(input("Enter any number for finding square root : "))
    sqr_root = math.sqrt(user_input)
    return f"Square root of user input : {sqr_root}"

def power_number():
    user_input = input(input("Enter number of calculating square : "))
    sqr = user_input**2
    return f"{sqr} is the square of {user_input}"

def calculater():
    
    print("""
          1. Addition
          2. Subtraction
          3. Subtraction
          4. Multiplication
          6. Square root
          7. factorial
          8. Area of objects
          9. Exit
          """)
    
    choise = int(input("Enter your choise : "))
    
    if choise == 1:
        a = float(input("Enter value : "))
        b = float(input("Enter value : "))
        sum = a + b
        print(f"Sum = {sum}")
        
    elif choise == 2:
        pass
    
    elif choise == 3:
        pass
    
    elif choise == 4:
        pass
    
    elif choise == 5:
        pass
    
    elif choise == 6:
        pass
    
    elif choise == 6:
        pass
    
    elif choise == 7:
        pass
    
    elif choise == 8:
        pass
    
    elif choise == 9:
        pass
    
    
def factorial():
    fact = int(input("Enter number for calculate factorial : "))
    result = math.factorial(fact)
    return f"{result} is the factorila of {fact}"


print('''
 1️⃣ Area of circle using math.pi

2️⃣ Find square root of user input

3️⃣ Find power of number

4️⃣ Create calculator using math

5️⃣ Find factorial using library
      ''')

pick = int(input("Enter 1-5 for checking each question.: "))

if pick == 1:
    print(area_circle())
elif pick == 2:
    print(square_root())
elif pick == 3:
    print(power_number())
elif pick == 4:
    print(calculater())
elif pick == 5:
    print(factorial())
else:
    print("Invalid Choise.")