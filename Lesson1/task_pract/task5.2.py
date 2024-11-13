count = 0  # Инициализация суммы до цикла
while True:
    num = int(input("Number: "))
    if num == 0:
        print(f"Сумма введенных чисел: {count}")
        break
    else:
        count += num

        