# #Check the palindrome word

# word = input("Enter the word: ")

# #change string to list for chage the element
# revers_char = list(word)

# # set pointer left 0 and right n-1
# left = 0
# right = len(revers_char)-1

# # use while loop for checking left < right then swap
# while left<right:
    
#     # store left element in temp veriable
#     temp = revers_char[left]
#     # swap last element from first elemnet
#     revers_char[left] = revers_char[right]
#     # right element store in temp variable
#     revers_char[right] = temp
    
#     # increase the left or right pointer until complete loop
#     left += 1
#     right -=1
    
# #Recreate the string using the reversed list
# reversed_string = "".join(revers_char)

# #Shoe the original list
# print(f"Original Word {word}")

# # if original word == to reversed word 
# if word == reversed_string :
#     # print palindrome
#     print("Word is palindrome.")
# else:
#     # not palindrome
#     print("Word is not palindrome.")
    


def palind(word):
    
    word = word.lower()
    
    left = 0
    right = len(word)-1
    is_palindrome = True

    while left<right:
        if word[left] != word[right]:
            is_palindrome = False
            break
        
        left +=1
        right -=1

    if is_palindrome :
        print("Word is palindrome.")
    else:
        print("Word is not palindrome.")

word = input("Enter the word: ")
palind(word)