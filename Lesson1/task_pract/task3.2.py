def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

num1 = int(input("Число 1: "))
num2 = int(input("Число 2: "))
num3 = int(input("Число 3: "))

result = max_of_three(num1, num2, num3)
print(f"Наибольшее число: {result}")
