d = {"b": 2, "a": 1}

sorted_dict = {}

for key in sorted(d):
    sorted_dict[key] = d[key]

print(sorted_dict)