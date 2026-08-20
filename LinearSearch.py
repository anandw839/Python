def linear_search(lst, target):
 
    for index, value in enumerate(lst):
        if value == target:
            return index
 
    return None
 
 
 
result = linear_search([5, 3, 8, 1, 4, 6, 7, 2, 9], 4)
print("Found at index:", result)