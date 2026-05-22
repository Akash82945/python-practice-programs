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
    user_input = float(input("Enter number of calculating square : "))
    sqr = user_input**2
    return f"{sqr} is the square of {user_input}"

def calculater():
    while True:
        print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Square root
            6. factorial
            7. Area of objects
            8. Exit
            """)
        
        choise = int(input("Enter your choise : "))
        
        if choise == 1:
            a = float(input("Enter value : "))
            b = float(input("Enter value : "))
            sum = a + b
            print(f"Addition = {sum}")
            
        elif choise == 2:
            a = float(input("Enter value : "))
            b = float(input("Enter value : "))
            sub = a - b
            print(f"Subtraction = {sub}")
        
        elif choise == 3:
            a = float(input("Enter value : "))
            b = float(input("Enter value : "))
            mul = a * b
            print(f"Multiplication = {mul}")
        
        elif choise == 4:
            a = float(input("Enter value : "))
            b = float(input("Enter value : "))
            div = a / b
            print(f"Division = {div}")
        
        elif choise == 5:
            user_input = float(input("Enter Number for calculating square root : "))
            sqt = math.sqrt(user_input)
            print(f"{sqt} is the square root of {user_input}")
        
        elif choise == 6:
            input_fact = int(input("Enter for calculating factorial : "))
            fact = math.factorial(input_fact)
            print(f"{fact} is the factorial of {input_fact}")
        
        elif choise == 7:
            while True:
                print("""
                      1. Rectangle
                      2. Square
                      3. Triangle
                      4. Circle
                      5. Exit
                      """)
                
                choise = int(input("Enter your choise : "))
                if choise == 1:
                    print("Calculating the Area of Rectangle.")
                    lenght = float(input("Enter value of lenght : "))
                    width = float(input("Enter value of width : "))
                    area_rectangle = lenght * width
                    print(f"{area_rectangle} is the Area of Recrtangle.")
                elif choise == 2:
                    print("Calculating the Area of Square.")
                    side = float(input("Enter value of side : "))
                    area_square = side **2
                    print(f"Area of square : {area_square}")
                elif choise == 3:
                    print("Calculating the Area of Triangle.")
                    base = float(input("Enter base value: "))
                    height = float(input("Enter height value: "))
                    area_triangle = 0.5*base*height
                    print(f"{area_triangle} is Area of Triangle.")
                elif choise == 4:
                    print("Calculating the Area of Circle.")
                    radius = float(input("Enter radius value : "))
                    area_circle = math.pi*(radius*radius)
                    print(f"{area_circle} is the Area of Circle.")
                else:
                    print("Invalid Choise.")
            
        
        elif choise == 8:
            break
    return
        
    
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