# def lcm(Number):
    
#     max_number = max(Number)
    
#     condition = max_number
    
#     while True:
#         is_lcm = True
#         for num in Number:
#             if condition % num !=0:
#                 is_lcm=False
#                 break
#         if is_lcm == True:
#             return condition
        
#         condition = condition + max_number
        
# number = input("Enter the array: ")
# n_number = [int(x) for x in number.split()]
# result = lcm(n_number)

# print(f"LCM {result}")





# Function 1: GCD (HCF) nikalne ke liye Euclidean Algorithm ka use
def get_gcd(a, b):
    while b != 0:
        remainder = a % b  # 1. Dono ka remainder nikalo
        a = b              # 2. b ko naya 'a' banao
        b = remainder      # 3. remainder ko naya 'b' banao (Jab tak b zero na ho)
    return a

# Function 2: Do numbers ka LCM nikalne ka mathematical formula
def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    # Formula: (a * b) / GCD(a, b) -> Yeh loop se fast hota hai
    return (a * b) / get_gcd(a, b)

# Function 3: Poore array par "Chain Logic" chalane ke liye
def find_array_lcm(my_array):
    # Logic: Pehle number ko shuruati result maan lo
    result = my_array[0] 
    
    # Loop: Index 1 se lekar aakhiri number tak ek-ek karke jao
    for num in range(1, len(my_array)):
        current_number = my_array[num]
        
        # Memory Logic: Purane 'result' aur 'current_number' ka LCM nikal kar 
        # use wapas 'result' mein update kar do (Cumulative LCM)
        result = get_lcm(result, current_number)
        
    return result

# --- Main Execution ---
my_array = input("Enter the array (space separated): ")
# List Comprehension: String input ko integers ki list mein badalna
new_array = [int(x) for x in my_array.split()]

# Function call aur final answer print
Result_lcm = find_array_lcm(new_array)
print(f"LCM of the array is: {Result_lcm}")