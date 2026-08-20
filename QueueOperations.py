# Queue class
class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list
    
    def enqueue(self, item):
        self.items.append(item)  # Append the item to the list
        
    def dequeue(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items.pop(0)  # Remove and return the first element
        
    def front(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items[0]  # Return the first element
    
    def is_empty(self):
        return len(self.items) == 0  # True if empty, otherwise False
    
    def display(self):
        print(self.items)  # Print the list items
 
# Create a Queue
q = Queue()
 
# Enqueue elements
q.enqueue(1)  # Adding 1 to the queue
q.enqueue(2)  # Adding 2 to the queue
q.enqueue(3)  # Adding 3 to the queue
 
# Display the queue
q.display()  # Output: [1, 2, 3]
 
# Dequeue elements
print(q.dequeue())  # Output: 1 (removing front element)
q.display()  # Output: [2, 3]
 
# Front element
print(q.front())  # Output: 2 (front element)
 
# Check if queue is empty
print(q.is_empty())  # Output: False (queue is not empty)