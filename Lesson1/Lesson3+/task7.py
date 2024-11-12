digit_input = int(input("Введи число: "))

# Проверка на простоту
if digit_input <= 1:
    print("Число не простое")
else:
    for i in range(2, digit_input // 2 + 1):
        if digit_input % i == 0:
            print("Число не простое")
            break
    else:
        print("Число простое")

