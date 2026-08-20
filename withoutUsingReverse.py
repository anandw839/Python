def reverse_word(word):
    reverse_word = ''
    for char in word:
        reverse_word = char + reverse_word
    return reverse_word
    
print(reverse_word("Python"))