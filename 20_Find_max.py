n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    lst.append(val)

max_val = lst[0]

for i in lst:
    if i > max_val:
        max_val = i

print("Maximum =", max_val)