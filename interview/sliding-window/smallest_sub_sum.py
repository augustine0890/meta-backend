"""
Smallest subarray with a given sum
Tim O(n) and Space O(1)
"""


def smallest_length_subarray_sum(array, target_sum):
    min_length = float("inf")  # Represents infinity
    sub_sum, w_start = 0, 0

    for w_end in range(len(array)):
        sub_sum += array[w_end]
        while sub_sum >= target_sum:
            min_length = min(min_length, w_end - w_start + 1)
            sub_sum -= array[w_start]
            w_start += 1

    return min_length if min_length != float("inf") else 0


print(smallest_length_subarray_sum([4, 1, 5, 2, 4, 1], 7))
print(smallest_length_subarray_sum([1, 5, 4, 2, 1, 8], 7))
print(smallest_length_subarray_sum([], 7))
