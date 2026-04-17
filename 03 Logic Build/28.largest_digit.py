num = int(input("Enter the number: "))

temp = num
max_digit = 0

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit += digit
    temp //= 10
    
print(max_digit)