#step 1: get ascii values for each character
#result
#step 3: check ascii value between 97 to 122 
#if any character present in them then convert them to uppercase
#code - 32 for uppercse
# ascii number convert to character
# else any character was already upper then add in main sentence 
# return result

def convert_to_upper(sentence):
    
    result = ""
    
    for char in sentence:
        code = ord(char)
        
        if code >= 97 and code <= 122:
            upper_code = code - 32
            upper_char = chr(upper_code)
            result+= upper_char
            
        else:
            result += char
            
    return result

sentence = input("Enter the sentence: ")
result= convert_to_upper(sentence)

print(f"Origial sentence ({sentence})")
print(f"Uppercase sentence ({result})")