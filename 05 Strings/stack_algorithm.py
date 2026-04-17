def reverse_string_stack(word):
    
    stack = []
    
    for i in word:
        stack.append(i)
        
    reverse_word= ""
    
    while len(stack)>0:
        pop_char = stack.pop()
        reverse_word += pop_char
        
    return reverse_word

word = input("Enter the word: ").lower()
result = reverse_string_stack(word)

print(f"Original word {word}")
print(f"Reversed string {result}")

# Check Palindrome
if word == result:
    print("Word is palindrome.")
else:
    print("Word is not palindroame.")