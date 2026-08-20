numbers = []
 
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
 
print("Queue after enqueues:", numbers)  # Output: Queue after enqueues: [1, 2, 3, 4]

print("Dequeued element:", numbers.pop(0))  # Output: Dequeued element: 1

print("Front of queue:", numbers[0])  # Output: Front of queue: 2

print("Is queue empty?", not bool(numbers))  # Output: Is queue empty? False