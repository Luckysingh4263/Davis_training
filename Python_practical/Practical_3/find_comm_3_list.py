def common_elements(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))

print(common_elements([1, 2, 3], [2, 3, 4], [2, 5, 3]))