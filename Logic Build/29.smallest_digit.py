num = int(input("Enter the number: "))

temp = num 
smallest_digit = 9

while temp > 0:
    digit = temp % 10
    if digit < smallest_digit:
        smallest_digit = digit
    temp //= 10
    
print(smallest_digit)