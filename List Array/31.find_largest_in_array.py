# List me largest number find karo.


n = int(input("Enter length of array: "))
array = []

for i in range(n):
    i = int(input("Enter value: "))
    array.append(i)
    
print("Array: ",array)


if len(array) == 0:
    print("The array is empty.")
else:
    largest = array[0]
    
    for x in array:
        if x>largest:
            largest = x

print(f"The largest number in this array {largest}")