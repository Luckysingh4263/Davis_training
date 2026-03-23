def merge_sort_unique(l1, l2):
    return sorted(set(l1 + l2))

print(merge_sort_unique([3, 1, 2], [2, 4, 5]))