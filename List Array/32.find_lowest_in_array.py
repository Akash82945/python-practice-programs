n = int(input("Enter the lengthe of array: "))

array = []

for i in range(n):
    i = int(input("Enter the values: "))
    array.append(i)
    
print(array)

if len(array) == 0:
    print("The array is empty.")
    
else:
    smallest_number = array[0]
    
    for x in array:
        if x<smallest_number:
            smallest_number = x
        
print(f"The smallest number in this array {smallest_number}")            
            