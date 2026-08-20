# Define the number of rows
n = 5
 
# The outer loop is for handling the number of rows
for i in range(n):
    # The inner loop is for handling the number of columns
    for j in range(i + 1):
        # print an asterisk without going to a new line
        print('*', end = '')
    # Print a newline character after each row
    print()