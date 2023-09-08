# Find the first integer which is unique in the list.
"""
Time complexity: O(n) + O(n) = O(n)
Dictionary can have at most n entries -> Space complexity: O(n)
"""


def find_first_unique(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for item in lst:
        if counts[item] == 1:
            return item

    return None


print(find_first_unique([9, 2, 3, 2, 6, 6]))
print(find_first_unique([4, 5, 1, 2, 0, 4]))
