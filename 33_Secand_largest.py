lst = [10, 20, 5, 15]

max1 = max(lst)
max2 = None

for i in lst:
    if i != max1:
        if max2 is None or i > max2:
            max2 = i

print(max2)