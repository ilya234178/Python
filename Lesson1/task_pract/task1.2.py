def add(a,b):
    return a + b
def subsrtact(a,b):
    return a - b

number1 = int(input("Введи первое число: "))
number2 = int(input("Введи второе число: "))

result_add = add(number1,number2)
result_sub = subsrtact(number1,number2)

print(f"Сумма чисел {number1} и {number2} равна {result_add}")
print(f"Разность чисел {number1} и {number2} равна {result_sub}")