def find_pairs(arr1, arr2, target):
    # Convert the array to set is O(1) time
    set1 = set(arr1)
    pair = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pair.append((complement, num))

    return pair


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)
