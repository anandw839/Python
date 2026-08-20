import string
def count_uppercase_letters(text):
    count = 0
    for char in text:
        if char in string.ascii_uppercase:
            count += 1
    return count

print(count_uppercase_letters('Hello WORLD'))