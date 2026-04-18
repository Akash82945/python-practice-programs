class calculater():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_input(self):
        self.x = int(input("Enter Value of x : "))
        self.y = int(input("Enter Value of y : "))
        
    def addition(self):
        sum = self.x + self.y
        return sum
    
    def subtraction(self):
        sub = self.x - self.y
        return sub
    
    def multiplication(self):
        mul = self.x * self.y
        return mul
    
    def division(self):
        while True:
            if self.y == 0:
                print("Error! Zero Division Not Possible. Try Again")
            else:
                div = self.x / self.y
            return div
    
    def square(self):
        user_input = int(input("Enter number for finding square : "))
        square = user_input * user_input
        return square
    
    
    def result(self):
        print("=== Simple Calculater ===")
        print("\nChoose the Operater:")
        print(f'''
              1. Addition
              2. Subtraction
              3. Multiplication
              4. Devision
              5. Check Square
              6. Clear
              7. Exit''')
        
        while True:
            choise = int(input("Choose any One [1/2/3/4/5/6/7] : "))
            if choise == 1:
                print( f"\nAddition : {self.addition()}")
            elif choise == 2:
                print( f"\nSubtraction : {self.subtraction()}")
            elif choise == 3:
                print( f"\nMultiplication : {self.multiplication()}")
            elif choise == 4:
                print( f"\nDivision : {self.division()}") 
            elif choise == 5:
                print( f"\nSquare : {self.square()}")
            elif choise == 6:
                self.x ,self.y = 0 , 0
                print("Result Clear.")
            elif choise == 7:
                break
            else:
                print("Invalid Choise")
        
            
    
    
num1 = calculater()
print(num1.get_input())
print(num1.result())