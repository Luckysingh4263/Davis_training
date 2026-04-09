lst = [1, 1, 2, 3]
result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)