def item_in_common(list1, list2):
    my_map = {}
    for i in list1:
        my_map[i] = True
    for j in list2:
        if j in my_map:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(item_in_common(list1, list2))
