def find_max_min(t):
    max_val = t[0]
    min_val = t[0]
    
    for i in t:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    
    return max_val, min_val

t = (5, 1, 8, 3)
max_val, min_val = find_max_min(t)

print("Max =", max_val, ", Min =", min_val)