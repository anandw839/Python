def reverse_list(list):
    start= 0
    end = len(list)-1
    
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    return list
    
# Testing the function with examples
print(reverse_list([10, 20, 30]))      # Output: [30, 20, 10]
print(reverse_list([5, 15, 25, 35]))   # Output: [35, 25, 15, 5]
print(reverse_list([1]))