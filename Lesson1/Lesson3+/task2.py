input_digit = int(input("Введите число: "))
count = 0  # Переменная для накопления суммы четных чисел

for i in range(input_digit + 1):
    print(i)  # Используем range(input_digit + 1) для включения числа input_digit
    if i % 2 == 0:  # Проверяем, является ли число четным
        count += i  # Добавляем четное число к общей сумме

print("Сумма всех четных чисел от 0 до", input_digit, "равна:", count)

