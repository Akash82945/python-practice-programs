def remove_space(sentence):
    new_word = ""
    
    for char in sentence:
        if char != " ":
            new_word += char
    
    return new_word

sentence = input("Enter the sentence: ")
result = remove_space(sentence)
print(result)
