num = int(input("Enter the number: "))

total = 0
count = 1

if num == 0:
    count =1
    total = 0
else:
    temp_num = abs(num)
    while temp_num > 0:
        digit = temp_num % 10
        total += digit
        
        temp_num //=10
        count +=1
        
print(total)