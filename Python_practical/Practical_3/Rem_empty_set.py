def remove_empty_sets(lst):
    return [s for s in lst if s]

print(remove_empty_sets([{1, 2}, set(), {3, 4}, set()]))