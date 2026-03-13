n = int(input("Enetr the range of array: "))

array = []

for i in range(n):
    i = int(input("Enter the values: "))
    array.append(i)
print(f"Original array {array}")
    
    
if len(array) == 0:
    print("The array is empty:")

else:
    even = []
    for x in array:
        if x %2 ==0:
            even.append(x)
print(f"Even numbers {even}")