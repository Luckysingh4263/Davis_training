def remove_common(list1, list2):
    return [x for x in list1 if x not in list2]

print(remove_common([1, 2, 3, 4], [3, 4, 5]))