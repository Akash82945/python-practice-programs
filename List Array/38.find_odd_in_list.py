n = int(input("Enter the elngth of array: "))

array = []

for i in range(n):
    i = int(input("Enter the values: "))
    array.append(i)

print(f"Original array {array}")

if len(array) == 0:
    print("The array is empty.")
else:
    odd = []
    for x in array:
        if x % 2 != 0:
            odd.append(x)
print(f"Odd numbers {odd}")