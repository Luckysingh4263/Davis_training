def tuple_frequency(t):
    freq = {}
    
    for i in t:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    return freq

print(tuple_frequency((1, 2, 2, 3, 1, 4)))