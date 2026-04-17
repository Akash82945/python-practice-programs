print("Calculate average of 1 to n")

num = int(input("Enter the number: "))
sum = 0

for i in range(1,num+1):
    sum += i

average = sum / num

print(f"Average of num {average}")