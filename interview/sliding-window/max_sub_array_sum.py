# Time: O(n) and Space O(1)
def max_sub_array_sum(array, k):
    if k > len(array) or k <= 0:
        return None

    max_sum = sub_sum = sum(array[:k])

    for i in range(k, len(array)):
        sub_sum = sub_sum - array[i - k] + array[i]
        if sub_sum > max_sum:
            max_sum = sub_sum

    return max_sum


print(max_sub_array_sum([1, 5, -1, 6, 3, 2], 3))
print(max_sub_array_sum([4, 2, 3, 5, 1], 2))
