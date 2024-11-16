count = 0
for _ in range(3):
    digit_input = int(input("Введи число: "))
    count += digit_input

average = count / 3  # Рассчитываем точное среднее значение

print(f"Среднее значение: {average}")

if average <= 10:
    print("Среднее значение меньше или равно 10")
else:
    print("Среднее значение больше 10")
