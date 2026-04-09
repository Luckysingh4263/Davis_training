def list_to_tuple(lst):
    return tuple(set(lst))

print(list_to_tuple([1, 2, 2, 3, 4, 4]))