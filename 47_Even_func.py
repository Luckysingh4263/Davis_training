def get_even(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result

print(get_even([1, 2, 3, 4]))