def max_of_three(a,b,c):
    if a > b and a >c:
        return a
    elif a < b and b > c:
        return b
    else:
        return c
    
num1 = int(input("Число1: "))
num2 = int(input("Число2: "))
num3 = int(input("Число3: "))

result = max_of_three(num1, num2 , num3)
print(result)