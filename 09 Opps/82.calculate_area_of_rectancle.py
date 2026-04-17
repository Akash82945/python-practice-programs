class Rectangle():
    
    def __init__(self,lenght,breath):
        self.length = lenght
        self.breath = breath
        
    def area(self):
        return f"Area of Rectangle {self.length*self.breath}"
    
rectangle1 = Rectangle(2,4)
rectangle2 = Rectangle(37,654)

print(rectangle1.area())
print(rectangle2.area())