lst = [1, 2, 4, 5]

n = len(lst) + 1
total = n * (n + 1) // 2
sum_lst = sum(lst)

print(total - sum_lst)