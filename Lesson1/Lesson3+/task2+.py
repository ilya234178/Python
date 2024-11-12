input_digit = int(input("Введите число: "))
count = 0  # Переменная для накопления суммы четных чисел
even_count = 0
for i in range(input_digit + 1):
    print(i)  # Используем range(input_digit + 1) для включения числа input_digit
    if i % 2 == 0:  # Проверяем, является ли число четным
        count += i  # Добавляем четное число к общей сумме
        even_count +=1

print("Сумма всех четных чисел от 0 до", input_digit, "равна:", count)
print("Количество четных чисел от 0 до", input_digit, "равно:", even_count)
