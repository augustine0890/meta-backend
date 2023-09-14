"""
The fibonacci sequence is a series of numbers where each number is the sum of two preceding ones
"""

# Time: O(2^n) (inefficient for large numbers due to exponential time complexity)
# Space: O(n) (maximum depth of the recursion tree)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Time: O(n)


def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


print(fibonacci_iterative(15))
print(fibonacci_sequence(15))
print(fibonacci_sequence(7))
