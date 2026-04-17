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
    