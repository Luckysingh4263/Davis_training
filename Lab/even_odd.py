def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Main Program
number = int(input("Enter a number: "))

result = even_odd(number)

print("The number is Even:", result)