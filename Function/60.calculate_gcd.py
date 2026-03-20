# Function 1: Do numbers ka GCD nikalne ke liye (Euclidean Algorithm)
def calculate_GCD(a, b):
    # Jab tak chota number (b) zero nahi ho jata, loop chalega
    while b != 0:
        remainder = a % b  # 1. Dono ka sheshphal (remainder) nikalo
        a = b              # 2. b ko naya 'a' banao (Badi value shift karo)
        b = remainder      # 3. remainder ko naya 'b' banao (Choti value shift karo)
    return a

# Function 2: Poore array ka GCD nikalne ke liye (Cumulative Logic)
def array_gdc(my_array):
    # Step 1: Array ke pehle element ko 'current_gcd' maan lo
    current = my_array[0]
    
    # Step 2: Index 1 se lekar aakhiri element tak loop chalao
    for num in range(1, len(my_array)):
        next_val = my_array[num] # Agla number uthao
        
        # Step 3: Pichle answer (current) aur naye number (next_val) ka GCD nikalo
        # Memory Update: 'current' variable naye GCD se overwrite ho jayega
        current = calculate_GCD(next_val, current)
        
    return current

# --- Input aur Execution ---
my_array = input("Enter the array (space separated): ")

# String input ko integers ki list mein badalna
new_array = [int(x) for x in my_array.split()]

# Array function ko call karna
result = array_gdc(new_array)

print(f"The GCD of the entire array is: {result}")