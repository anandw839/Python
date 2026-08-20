def reorder_and_eliminate_middle(words):
    # Handle edge cases
    if len(words) <= 2:
        return []
    
    # Sort the words by length in descending order
    sorted_words = sorted(words, key=len, reverse=True)
    
    # Calculate the middle index
    middle = len(sorted_words) // 2
    
    # Delete the middle element(s)
    if len(sorted_words) % 2 == 0:
        del sorted_words[middle-1:middle+1]
    else:
        del sorted_words[middle]
    
    # Return the reordered list with the middle element(s) removed
    return sorted_words
    
    
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))  
# Output: ["banana", "grapes", "mango", "kiwi"]