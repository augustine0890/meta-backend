# Find the second maximum element in the list
# Time complexity: O(n)
def find_second_maximum(lst):
    if len(lst) <= 1:
        return None

    max_val, second_max_val = float('-inf'), float('-inf')
    for item in lst:
        if isinstance(item, (int, float)):
            if item > max_val:
                second_max_val = max_val
                max_val = item
            elif item > second_max_val and item != max_val:
                second_max_val = item

    return second_max_val


print(find_second_maximum([1, 2, 3, 6]))
print(find_second_maximum([6]))
print(find_second_maximum([3, 6]))
print(find_second_maximum([6, 3]))
print(find_second_maximum([0, 1, 2, 3]))
print(find_second_maximum([0, 1, 2, 3]))
print(find_second_maximum([0, -1, -2, -3]))
print(find_second_maximum([1, "two", 3]))
