def pair_sum(t, target):
    result = []
    
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] + t[j] == target:
                result.append((t[i], t[j]))
    
    return result

print(pair_sum((1, 2, 3, 4, 5), 5))