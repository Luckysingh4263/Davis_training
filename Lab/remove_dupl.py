# lst = [1, 2, 3, 2, 4, 2, 5]

# x = int(input("Enter number to remove duplicates of: "))

# seen = False
# result = []

# for i in lst:
#     if i == x:
#         if not seen:
#             result.append(i)
#             seen = True
#     else:
#         result.append(i)

# print("Original list:", lst)
# print("After removing duplicate of", x, ":", result)



# arr = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2, 8, 9, 2, 10, 2]
# x = int(input("Enter number to search: "))
# if x in arr:
#     first = arr.index(x)   
#     i = 0
#     while i < len(arr):
#         if arr[i] == x and i != first:
#             arr.pop(i)
#         else:
#             i += 1

#     print("Updated list:", arr)
# else:
#     print("Number not found")

# Step 1: Create a list of 15 numbers
numbers = [5, 2, 7, 2, 9, 2, 4, 6, 2, 8, 1, 3, 2, 10, 11]

# Step 2: Take user input
num = int(input("Enter a number to search and modify: "))

# Step 3 & 4: Remove all occurrences except first
found = False
result = []

for i in numbers:
    if i == num:
        if not found:
            result.append(i)   # keep first occurrence
            found = True
        # skip other occurrences
    else:
        result.append(i)

# Step 5: Output result
print("Original List:", numbers)
print("Updated List:", result)