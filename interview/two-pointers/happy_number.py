"""
Determine if a number n is a happy number
- Sum of the squares of its digits
- Repeat process until:
    - The number equal 1
    - It enters a cycle --> not happy number
Time complexity: O(n)
Space complexity: O(1)
"""

# Time O(n) worst case, and space complexity O(n)


def naive_is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squared_digits(n)
    return n == 1


def is_happy_number(n):
    slow_pointer = n
    fast_pointer = sum_of_squared_digits(n)
    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(
            sum_of_squared_digits(fast_pointer))
    if fast_pointer == 1:
        return True
    return False


def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit**2
    return total_sum


inputs = [1, 5, 19, 25, 7]
for i in range(len(inputs)):
    print(i+1, ".", "Input Number: ", inputs[i], sep="")
    print("\n\tIs it a happy number? (Naive Approach)",
          naive_is_happy(inputs[i]))
    print("\n\tIs it a happy number? ", is_happy_number(inputs[i]))
    print("-" * 10)
