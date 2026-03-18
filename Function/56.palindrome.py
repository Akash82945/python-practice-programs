def palindrome(number):
    # Original number ko 'temp' mein save kiya taaki comparison ke liye 'number' safe rahe
    temp = number 
    
    # Isme hum number ko ulta (reverse) karke store karenge
    reversed_num = 0
    
    # Loop tab tak chalega jab tak saare digits khatam na ho jayein
    while temp > 0:
        # 1. Aakhiri digit nikaalo (e.g., 121 % 10 = 1)
        digit = temp % 10
        
        # 2. Reverse number ko update karo (Pichle number ko 10 se multiply karke naya digit jodo)
        # Logic: (0*10)+1 = 1 -> (1*10)+2 = 12 -> (12*10)+1 = 121
        reversed_num = (reversed_num * 10) + digit
        
        # 3. Number ko chhota karo (Aakhiri digit hatao)
        temp //= 10
        
    # Check karo: Kya asli number aur ulta kiya hua number barabar hain?
    return number == reversed_num

# User se input lena
number = int(input("Enter the number: "))

# Function call karke result check karna
if palindrome(number):
    print("Palindrome")
else:
    print("Not palindrome")