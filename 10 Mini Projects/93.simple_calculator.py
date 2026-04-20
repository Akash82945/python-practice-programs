class Calculater():
    
    def __init__ (self):
        self.x = 0
        self.y = 0
        
    def get_input(self):
        self.x = int(input("Enter first value: "))
        self.y = int(input("Enter second value: "))
        return
    
    def y_input(self):
        self.y = int(input("Enter second value: "))
        return
    
    def add(self):
        return self.y + self.x
    
    def sub(self):
        return self.x - self.y
    
    def mul(self):
        return self.x * self.y
    
    def div(self):
        if self.y == 0:
            self.y_input()
            
        else :
            return self.x / self.y
        
        
    def calculation(self):
        print(" ===== Sinple Calculater =====")
        print("Chooose the Operation which you performed.")
        print('''
              1. Addition
              2. Subtraction
              3. Multiplication
              4. Division
              5. Clear
              6. Exit
              ''')
        
        while True:
            choice = int(input("Enter your Operater [1/2/3/4/5/6]: "))
            if choice == 1:
                print(f"Addition : {self.x} + {self.y} = {self.add()}")
            elif choice == 2:
                print(f"Subtraction : {self.x} - {self.y} = {self.sub()}")
            elif choice == 3:
                print(f"Multiplication : {self.x} * {self.y} = {self.mul()}")
            elif choice == 4:
                print(f"Division : {self.x} / {self.y} = {self.div()}")
            elif choice == 5:
                self.x = 0
                self.y = 0
            elif choice == 6:
                break
            else:
                print("Invalid Choise! Try Again.")
            
num1 = Calculater()
num1.get_input()
print(num1.calculation())