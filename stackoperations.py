# Stack class
class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list
    
    def push(self, item):
        self.items.append(item)  # Append the item to the list
        
    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items.pop()  # Remove and return the last element
        
    def top(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items[-1]  # Return the last element
    
    def is_empty(self):
        return len(self.items) == 0  # True if empty, otherwise False
    
    def display(self):
        print(self.items)  # Print the list items
 
# Create a Stack
s = Stack()
 
# Push elements
s.push(1)  # Adding 1 to the stack
s.push(2)  # Adding 2 to the stack
s.push(3)  # Adding 3 to the stack
 
# Display the stack
s.display()  # Output: [1, 2, 3]
 
# Pop elements
print(s.pop())  # Output: 3 (removing top element)
s.display()  # Output: [1, 2]
 
# Top element
print(s.top())  # Output: 2 (top element)
 
# Check if stack is empty
print(s.is_empty())  # Output: False (stack is not empty)