# Find largest number in the Array.
def largest_number(lists):
    # original list ki ek copy banayi (u_list) taaki main list safe rahe
    u_list = list(lists)
    
    # Check kar rahe hain: Agar user ne kuch enter hi nahi kiya (Khali list)
    if len(lists) == 0:
        return "Empty list"
    
    else:
        # Step 1: Maan lo ki pehla number (index 0) hi 'largest' hai
        largest_number = u_list[0]  
        
        # Step 2: Loop chala kar list ke baaki numbers (num) ko check karenge
        for num in u_list:
            # Agar koi 'num' hamare 'largest_number' se bada milta hai...
            if num > largest_number:
                # ...toh 'largest_number' ko us naye bade number se badal do
                largest_number = num
                
        # Poori list chhanne ke baad sabse bada number wapas (return) karo
        return largest_number

# 1. User se numbers ki string lo (Example: "10 55 22")
lists = input("Enter the list (space separated): ")

# 2. String ko todkar aur numbers mein badalkar list banao
# lists.split() -> Har space par string ko todta hai ("10", "55", "22")
# [int(x) for x...] -> Har ek tukde ko Integer mein convert karke list mein dalta hai
n_list = [int(x) for x in lists.split()]

# 3. Function ko taiyaar list (n_list) bhejo aur result receive karo
result = largest_number(n_list)

# 4. Final Result print karo
print(f"Largest number {result}")