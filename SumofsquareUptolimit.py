def sum_of_squares_upto_limit(limit):
    i=1
    sum = 0
    while i * i <= limit:
        sum += i * i
        i += 1
    return sum
    
print(sum_of_squares_upto_limit(30))