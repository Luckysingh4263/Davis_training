def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for i in lst:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))