num = int(input("Enter the number: "))

count = 0

if num == 0 :
    count = 1
else:
    temp_num = abs(num)
    while temp_num > 0:
        temp_num //=10
        count += 1

print(count)
    