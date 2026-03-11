# # Reverse Number


num = int(input("Enter the number: "))

reverse_number = 0

while num > 0:
    last_digit = num % 10
    reverse_number = (reverse_number*10)+last_digit
    num = num // 10
    
print(reverse_number)