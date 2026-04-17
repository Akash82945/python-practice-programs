# # User se array ki length (kitne numbers honge) input lena
# n = int(input("Enter the length of array: "))

# # Khali list (array) create karna values store karne ke liye
# array = []

# # Loop chala kar user se 'n' baar values lena aur array mein add karna
# for i in range(n):
#     val = int(input("Enter the values: "))
#     array.append(val)

# print(f"Your original array {array}")

# # Edge case check: Agar array khali ho toh aage ka process na chale
# if len(array) == 0:
#     print("The array is empty.")
# else:
#     # --- BUBBLE SORT LOGIC STARTS HERE ---
    
#     # Outer Loop: Ye loop 'n' baar chalega taaki har number apni sahi jagah pahunch sake
#     for x in range(n):
        
#         # Inner Loop: Ye padosi (adjacent) numbers ko compare karta hai
#         # 'n-x-1' ka matlab hai ki sorted numbers ko dobara check nahi karna
#         for j in range(0, n - x - 1):
            
#             # Condition: Agar left side wala number right side wale se bada hai
#             if array[j] > array[j+1]:
                
#                 # Swapping Logic: Do numbers ki jagah aapas mein badalna
#                 temp = array[j]       # Left value ko temp mein surakshit (save) rakha
#                 array[j] = array[j+1] # Right value ko left position par move kiya
#                 array[j+1] = temp     # Temp se purani left value ko right position par dala

# # Final sorted array ko print karna
# print(f"Sorted array {array}")




# n = int(input("Enter the elngth of array: "))

# array = []

# for i in range(n):
#     i = int(input("Enter the values: "))
#     array.append(i)

# print(f"Original array {array}")

# if len(array) == 0:
#     print("The array is empty.")
# else:
    
#     for x in range(n):
#         main_index = x
#         for j in range(x+1,n):
            
#             if array[j] < array[main_index]:
#                 main_index = j
#         array[x], array[main_index] = array[main_index], array[x]
        
# print(f"Sorted array {array}")




# Bubbole Sort or Selection sort both

# Function for bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range (0,n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# Function for selection sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[j] < min_index:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
    return array

# Mian program
n = int(input("Enter the length of array: "))
original_array = []

for x in range(n):
    original_array.append(int(input(f"Values {x+1}")))
    
print(f"Original array {original_array}")
print("1. Bubble sort")
print("2. Selection srot")

choice = int(input("Choose the algorithms. {1/2}"))

temp_array = original_array.copy()
if choice == 1:
    result = bubble_sort(temp_array)
    print(f"Sorted array using bubble sort algorithm: {result}")
elif choice == 2:
    result = selection_sort(temp_array)
    print(f"Sorted array using selection sort algorithm: {result}")
else:
    print("Invalit choice.")