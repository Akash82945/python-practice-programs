def largest_character(sentence):
    word_list = sentence.split()
    
    longest = word_list[0]
    
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = input("Enter the sentence: ")
result = largest_character(sentence)
print(f"The largest word id ({result})")