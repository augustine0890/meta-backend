def find_duplicates(array):
    freq_table = {}
    duplicates = []
    for num in array:
        if num in freq_table:
            if freq_table[num] == 1:
                duplicates.append(num)
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    return duplicates


print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))
