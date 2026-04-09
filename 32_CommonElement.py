lst1 = [1, 2, 3]
lst2 = [2, 3, 4]

common = []

for i in lst1:
    if i in lst2 and i not in common:
        common.append(i)

print(common)