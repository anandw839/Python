numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
 
print(len(numbers))  # Output: 10
 
print(numbers[2])    # Output: 'Two'
 
print(numbers[2:6])  # Output: ['Two', 'Three', 'Four', 'Five']

print(numbers[:6])  # Output: ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
print(numbers[3:])  # Output: ['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

print(numbers[1:8:2])  # Output: ['One', 'Three', 'Five', 'Seven']
print(numbers[1:8:3])  # Output: ['One', 'Four', 'Seven']
print(numbers[::3])    # Output: ['Zero', 'Three', 'Six', 'Nine']

print(numbers[::-1])   # Output: ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
print(numbers[::-3])   # Output: ['Nine', 'Six', 'Three', 'Zero']

del numbers[3:]
print(numbers)         # Output: ['Zero', 'One', 'Two']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[3:7] = [3, 4, 5, 6]
print(numbers)        # Output: ['Zero', 'One', 'Two', 3, 4, 5, 6, 'Seven', 'Eight', 'Nine']