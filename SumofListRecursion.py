def sum_of_list(lst, n):
    print(f"Calculating sum of first {n} elements of {lst}")
    if n == 0:
        print("Reached base case: sum is 0")
        return 0
    result = lst[n-1] + sum_of_list(lst, n-1)
    print(f"Sum of first {n} elements is {result}")
    return result
 
# Running the step-by-step example
result = sum_of_list([1, 2, 3], 3)
print(f"Final Output: Sum of list is {result}")