# Given a list and a number "k", find two numbers from the list that sum to "k".
# TIme complexity O(n2) and space O(1)
def find_sum(lst, k):
    for i, num1 in enumerate(lst):
        for num2 in lst[i+1:]:
            if num1 + num2 == k:
                return [num1, num2]
    return None

# Time: O(n) and Space: O(n) - store all numbers in the list
def find_sum2(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return [k-num, num]
        seen.add(num)
    return None

print(find_sum([1,21,3,14,5,60,7,6], 81))
print(find_sum2([1,21,3,14,5,60,7,6], 81))
