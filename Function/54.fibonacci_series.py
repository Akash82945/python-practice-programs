def fibonacci(number):
    
    if number <0:
        return []
    
    fib = [0,]
    
    a,b = 0,1
    
    if number == 1:
        return fib
    
    for num in range (number-1):
        a,b = b,a+b
        fib.append(a)
    return fib
        
        
print(fibonacci(int(input("Enter the number: "))))