# Arrange elements in such a way that the maximum element appears at first position,
# then minimum at second, then second maximum at third and second minimum at fourth and so on.
# Time: O(n) and Space: O(n)
def max_min(lst):
    if len(lst) == 0:
        return None

    result = []
    i, j = 0, len(lst) - 1
    while i <= j:
        if i != j:
            result.append(lst[j])
            result.append(lst[i])
        else:
            result.append(lst[i])
        i += 1
        j -= 1
    return result


print(max_min([1, 2, 3, 4, 5]))
