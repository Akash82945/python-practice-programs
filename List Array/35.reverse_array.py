n = int(input("Enter the length of array: "))

array = []

for i in range (n):
    i = int(input("Enter the values: "))
    array.append(i)
    
print(array)

if len(array) == 0:
    print("The array is empty.")
else:
    reverse_array = []
    for x in array[::-1]:
        reverse_array.append(x)
        
print(f"This is the reverserd array {reverse_array}")