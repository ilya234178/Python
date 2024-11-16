def is_even(n):
    return n % 2 == 0  # Функция возвращает True, если n четное, и False, если нечетное

digit_input = int(input("Введи число: "))
if is_even(digit_input):  # Проверяем результат функции
    print(f"Число {digit_input} является четным.")
else:
    print(f"Число {digit_input} является нечетным.")

