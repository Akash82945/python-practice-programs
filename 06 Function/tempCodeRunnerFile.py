def fibonacci(number):
    
    fib = [0,]
    
    a,b = 0,1
    
    if number == 1:
        return a
    
    for num in range (0,number-1):
        a,b = b,a+b
        fib.append(a)
    return fib
        
        
print(fibonacci(int(input("Enter the number: "))))