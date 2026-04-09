sales = []

print("Enter 7 days sales:")
for i in range(7):
    val = int(input(f"Day {i+1}: "))
    sales.append(val)

total = 0
for i in sales:
    total += i

print("Total Sales =", total)