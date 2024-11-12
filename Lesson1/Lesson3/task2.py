password = 23111993
input_digit = int(input("Введите пароль: "))

while input_digit != password:  # Повторяем, пока пароль не совпадает
    print("Неверный пароль, попробуйте снова.")
    input_digit = int(input("Введите пароль: "))

print("Пароль верный!")  # Сообщение, когда пароль введен правильно

    
