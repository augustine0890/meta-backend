# Time: O(N), N is the number of elements in nums; Space O(N) store the elements in set
def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    max_length = 0

    for num in nums:
        # If it's the start of a sequence
        if num - 1 not in nums_set:
            length = 1
            while num + length in nums_set:
                length += 1
            max_length = max(length, max_length)
    return max_length


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive_sequence([]))
print(longest_consecutive_sequence([3]))
print(longest_consecutive_sequence([1, 2, 3, 4, 5]))
print(longest_consecutive_sequence([-1, -2, -3, 1, 2, 3]))
print(longest_consecutive_sequence([2, 2, 2, 2]))
