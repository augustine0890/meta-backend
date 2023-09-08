# Rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other
# Time: O(n2) and Space: O(n)
def rearrange(lst):
    result = []
    for item in lst:
        if item > 0:
            result.append(item)
        else:
            result = [item] + result  # take O(m) time (insert beginning)
    return result

# Iterates through with two pointers
# Time O(n) and Space O(1)


def rearrange2(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        while lst[left] < 0 and left < right:
            left += 1
        while lst[right] >= 0 and left < right:
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]

    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
print(rearrange2([10, -1, 20, 4, 5, -9, -6]))
