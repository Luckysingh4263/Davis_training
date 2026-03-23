def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([10, 20, 30, 40, 50], 2))