# Merge two sorted lists
# O(n + m) where n and m are the lengths of the lists
# Space: O(n)
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Append remaining elements of list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements of list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

    
print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))