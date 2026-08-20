def factorial(n):
 
    if n == 1:
        return 1
 
    return n * factorial(n - 1)
 
 
# Example usage
result = factorial(5)
print("Factorial of 5 is:", result)