"""
The time complexity is O(n), where n is the number of characters in the string.
The space complexity is O(1), use constant space to store two indexes
"""
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Examples
examples = ["level", "python", "radar", "world", "deified"]
for example in examples:
    print(f"'{example}' is a palindrome: {is_palindrome(example)}")
