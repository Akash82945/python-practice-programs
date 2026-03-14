# User se input lena (Example: "HELLO")
word = input("Enter the string: ")

# String ko list mein convert karna kyunki Python strings 'Immutable' (un-changeable) hoti hain
# List banane se hum characters ko aapas mein swap (adla-badli) kar payenge
reversed_string_list = list(word)

# Do pointers set karna: ek shuruat (left) aur ek aakhri (right) index par
left = 0
right = len(reversed_string_list) - 1

# Jab tak dono pointers beech mein nahi milte, tab tak loop chalega
while left < right:
    # 1. Swapping Logic: Left aur Right characters ki jagah badalna
    # Temp variable ka use karke value ko overwrite hone se bachana
    temp = reversed_string_list[left]
    reversed_string_list[left] = reversed_string_list[right]
    reversed_string_list[right] = temp
    
    # 2. Pointers Move karna: Left ko aage aur Right ko peeche le jana
    left += 1
    right -= 1

# Reversed list ke characters ko wapas ek single string mein jodna
# "" ka matlab hai ki characters ke beech mein koi gap nahi hoga
final_reversed = "".join(reversed_string_list)

# Output dikhana
print(f"Original Word: {word}")
print(f"Reversed Word: {final_reversed}")