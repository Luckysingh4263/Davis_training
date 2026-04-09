n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    lst.append(val)

count = 0
for i in lst:
    if i > 50:
        count += 1

print("Count =", count)