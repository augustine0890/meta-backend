# Given a list, for each element at index i, we want to find the product of all numbers in the list except the one at i.
# Time: O(n2) and Space: O(n)
def find_product(lst):
    result = []
    for ix in range(len(lst)):
        total = 1
        for jx in range(len(lst)):
            if jx != ix:
                total *= lst[jx]
        result.append(total)
    return result

# Time: O(n2) and Space: O(n)
"""
Mathematically, for an element at index i:
Result[i] = PrefixProduct[i] × SuffixProduct[i]
"""
def find_product2(lst):
    n = len(lst)
    output = [1] * n
    prefix_product = 1
    suffix_product = 1

    for i in range(n):
        output[i] *= prefix_product
        prefix_product *= lst[i]

    for i in range(n-1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= lst[i]
    return output


print(find_product([1,2,3,4]))
print(find_product2([1,2,3,4]))