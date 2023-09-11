# Find the contiguous sublist with the largest sum
# Time: O(n) and Space: O(1)
def find_max_sum_sublist(lst):
    if len(lst) == 0:
        return 0

    max_current = max_global = lst[0]
    for num in lst[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
