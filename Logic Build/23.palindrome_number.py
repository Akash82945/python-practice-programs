num = int(input("Enter the number: "))

s_num = str(num)

palin = s_num[::-1]

if s_num == palin:
   print(f"Yes! {s_num} is a palindrome because it reads as {palin} backward.")
else:
    print(f"No. {s_num} is not a palindrome (backward it is {palin}).")
    

num = int(input("Enter the number: "))

temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10
    reverse_num = (reverse_num*10)+digit
    temp//=10
    
if num==reverse_num:
    print(f"{num } is palindrome.")
else:
    print(f"{num} is not plindrome")