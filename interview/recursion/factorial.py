"""
Factorial of any integer - the product of all positive integers less than or equal to itself
"""

# Time: O(n) and Space: O(n)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Time: O(n) and Space: O(1)


def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(4))
print(factorial(1))
print(factorial(0))
print(factorial(5))
print(iterative_factorial(5))
print(iterative_factorial(0))
print(iterative_factorial(1))
