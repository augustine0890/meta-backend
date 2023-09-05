# Remove even integers from a list
# O(n)
def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

print(remove_even([1,2,4,5,10,6,3]))