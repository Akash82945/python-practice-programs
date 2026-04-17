n = int(input("Enter the length of array:"))
array = []

for i in range(n):
    i = int(input("Enter the values: "))
    array.append(i)

print(array)

if len(array) ==0:
    print("The array is empty.")
    
else:
    duplicate = []
    for x in range(len(array)):
        for j in range(x+1, len(array)):
            if array[x]== array [j]:
                duplicate.append(array[x])
                
print(f"Duplicate found {duplicate}")