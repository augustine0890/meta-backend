# Rotate its elements by one index from right to left
# Time complexity: O(n) <- O(k) and Space: O(n)
def right_rotate(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], 3))
