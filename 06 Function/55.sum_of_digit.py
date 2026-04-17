def sum_of_digit(number):
    # 'total' digits ka jod jama karega aur 'count' unki ginti rakhega
    total = 0 
    count = 0
    
    # Check kar rahe hain agar user ne 0 dala hai
    if number == 0:
        return 0,1
    
    else :
        # abs() function negative number ko positive mein badal deta hai
        temp_number = abs(number)
        
        # Jab tak number 0 se bada hai, loop chalta rahega
        while temp_number > 0:
            # 1. Modulo (%) se aakhiri digit nikaala (e.g., 5374 % 10 = 4)
            digit = temp_number % 10
            # 2. 'total' mein us digit ko joda
            total += digit
            
            # 3. Floor division (//) se aakhiri digit hata diya (e.g., 5374 // 10 = 537)
            temp_number //= 10
            # 4. Loop jitni baar chalega, utne digits count honge
            count += 1
                        
        # Function do values (Sum aur Count) ek saath return kar raha hai
        return total, count
    
# User se number input liya
number = int(input("Enter the number: "))

# Tuple Unpacking: Return ki gayi dono values ko alag variables mein store kiya
sum, count = sum_of_digit(number)

# F-string ka use karke result print kiya
print(f"Sum ({sum}) of this number {number}")
print(f"Count ({count}) of this number {number}")

# Example call:
# print(sum_of_digit(5374))