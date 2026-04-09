def total_bill(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(total_bill([100, 200, 300]))