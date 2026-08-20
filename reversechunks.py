def reverse_chunks(numbers):
    for i in range(0, len(numbers), 3):
        numbers[i:i+3] = numbers[i:i+3][::-1]
    return numbers
    
    
print(reverse_chunks([1, 2, 3, 4, 5, 6, 7, 8, 9]))  