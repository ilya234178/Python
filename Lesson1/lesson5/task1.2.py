def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False

num = int(input("Number: "))
result = is_even(num)
print(result)