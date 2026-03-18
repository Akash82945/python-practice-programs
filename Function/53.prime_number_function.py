def prime_number(number):
    
    is_prime = True
    
    if number <= 1:
        is_prime = False
        
    
    else:
        for num in range(2,number):
            if (number % num) == 0:
                is_prime = False
                return False
        
        return is_prime
    
print(prime_number(int(input("Enter number: "))))