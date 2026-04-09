s = input("Enter string: ").lower()
result = ""

for ch in s:
    if ch in "aeiou":
        result += "*"
    else:
        result += ch

print(result)