while True:
    age = int(input("Введи возраст: "))
    if age < 18:
        print("попробуй еще раз")
    else:
        print("Доступ открыт")
        break