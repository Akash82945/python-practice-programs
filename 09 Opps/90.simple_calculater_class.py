class calculater():
    
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        
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
        div = self.x / self.y
        return div
    
    def square(self):
        user_input = int(input("Enter number for finding square : "))
        self.x = user_input
        square = self.x * self.x
        return square
    
    def result(self):
        print("=== Simple Calculater ===")
        print("\nChoose the Operater:")
        print(f'''
              1. Addition
              2. Subtraction
              3. Multiplication
              4. Devision
              5. Check Square''')
        choise = int(input("Choose any One [1/2/3/4/5] : "))
        if choise == 1:
            return f"\nAddition : {self.addition()}"
        elif choise == 2:
            return f"\nSubtraction : {self.subtraction()}"
        elif choise == 3:
            return f"\nMultiplication : {self.multiplication()}"
        elif choise == 4:
            return f"\nDivision : {self.division()}" 
        elif choise == 5:
            return f"\nSquare : {self.square()}"
        else:
            return "Invalid Choise"
        
    
    
num1 = calculater(5,5)
print(num1.result())