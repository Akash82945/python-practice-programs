# function for check Prime number
def prime_number(number):
    # set prime number True
    is_prime = True
    
    # if number <= 1 set prime False
    if number <= 1:
        is_prime = False
        
    # else check each number from (2, n)
    # if given number is divide by itself number == 0
    # set is_prime is false
    # return false
    else:
        for num in range(2,number):
            if (number % num) == 0:
                is_prime = False
                return False
        
        # retrun is_prime
        return is_prime
    
# print(True for prime number or False for non_prime number)
print(prime_number(int(input("Enter number: "))))