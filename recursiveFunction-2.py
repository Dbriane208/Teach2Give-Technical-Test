"""
Write a recursive function to calculate the factorial of a number
"""

def recursiveFunction(n):
    # Base case for factorial should return 1
    if n == 1:
        return 1
    else:
        return (n * recursiveFunction(n-1))
    
print(recursiveFunction(3))  