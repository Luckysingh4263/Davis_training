lst = [1, 1, 2, 3, 3]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(len(unique))