num = int(input("Enter the number: "))

is_prime = True

#prime number is 2,3,5,7,11,13,17,19,.....
#Who number divided by 1 and itself called prime

if num <= 1:
    is_prime= False
else:
    for i in range(2,num):
        if(num%i)==0:
            is_prime=False
            break
if is_prime:
    print(f"{num} is Prime.")
else:
    print(f"{num} is not prime.")