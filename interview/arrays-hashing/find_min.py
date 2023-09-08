# Given a list of size  ‘n,’ can you find the minimum value in the list
# Linear time O(n)
def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

print(find_minimum([9,2,3,6]))