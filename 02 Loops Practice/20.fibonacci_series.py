num = int(input("Enter range of number: "))

a , b = 0 , 1
print("Fibonacci Series")
for i in range (1,num+1):
    print(i,". ", a)
    
    a , b = b , a+b

    

    