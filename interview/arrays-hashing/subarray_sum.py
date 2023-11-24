# Time O(N) and Space: O(N)
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0

    for idx, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            # This index is essentially the end of a previous subarray
            # right before the start of our target subarray
            return [sum_index[current_sum - target] + 1, idx]

        sum_index[current_sum] = idx
    return []


nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))
