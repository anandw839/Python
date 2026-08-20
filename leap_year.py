
def is_leap_year(year):
 
    if year < 1:
        return False
 
    if year % 4 != 0:
        return False
 
    if year % 100 != 0:
        return True
 
    if year % 400 != 0:
        return False
                    
    return True
 
# Test Cases:
print(is_leap_year(2000))  # Output: True
#print(is_leap_year(1900))  # Output: False