num = int(input("Enter the number: "))

order = len(str(num))
temp_num = num 
total = 0

while temp_num > 0:
    digit = temp_num % 10
    total += digit ** order
    temp_num //= 10
    
if num == total:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")
    
    
print("print armstrong number between 1-1000")

for i in range (1,1001):
    order = len(str(i))
    total = 0
    temp = i
    
    while temp > 0:
        digit = temp % 10
        total += temp ** order
        temp //= 10
        
    if i == total:
        print(i)
    