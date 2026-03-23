def flatten_list(lst):
    result = []
    for sublist in lst:
        for item in sublist:
            result.append(item)
    return result

print(flatten_list([[1, 2], [3, 4], [5]]))