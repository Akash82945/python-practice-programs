n = int(input("Enter the length of array: "))

array = []

for i in range (n):
    i = int(input("Enter the values: "))
    array.append(i)
    
print(array)

total = 0
if len(array) == 0:
    print("The array is empty.")
else:
    for x in array:
        total += x
        
average = total/n 

print(f"The average of this array {average}")