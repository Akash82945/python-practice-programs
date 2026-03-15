def word_count(sentence):
    clean_sentence = sentence.strip()
    
    if clean_sentence == 0:
        return 0
    
    else:
        new_sentence = clean_sentence.split()
        
    return len(new_sentence)

sentence = input("Enter the sentence: ")
result = word_count(sentence)
print(f"{result} words in this sentence.")