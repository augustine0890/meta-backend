# Time: O(k) + O(n-k) --> O(n)
# Space: O(n-k+1) --> O(n)
def sub_array_sum(array, k):
    if k > len(array):
        return []
    sub_sum = sum(array[:k])
    w_sum = [sub_sum]

    w_sum += [
        sub_sum := sub_sum - array[i - k] + array[i] for i in range(k, len(array))
    ]
    return w_sum


print(sub_array_sum([1, 5, -1, 6, 3, 2], 3))
