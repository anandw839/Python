def get_number_of_digits(number):
 
    if number < 0:
        return -1
 
    if number == 0:
        return 1
 
    number_of_digits = 0
 
    while number > 0:
        number //= 10
        number_of_digits += 1
 
    return number_of_digits

print(get_number_of_digits(123))
        