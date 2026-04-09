def tuple_to_dict(keys, values):
    return dict(zip(keys, values))

print(tuple_to_dict(('a', 'b', 'c'), (1, 2, 3)))