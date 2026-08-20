numbers = []
 
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
 
print("Stack after pushes:", numbers)  # Output: Stack after pushes: [1, 2, 3, 4]

print("Popped element:", numbers.pop())  # Output: Popped element: 4

print("Top of stack:", numbers[-1])  # Output: Top of stack: 3

print("Is stack empty?", not bool(numbers))  # Output: Is stack empty? False