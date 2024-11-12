names = []
ages = []

while True:
    name = input("Введите имя друга (или 'стоп' для завершения): ")
    if name.lower() == "стоп":
        break
    while True:
        age = int(input(f"Введите возраст {name}: "))
        if age < 0:
            print("Возраст не может быть отрицательным. Попробуйте еще раз.")
        else:
            break
    
    names.append(name)
    ages.append(age)
    # После выхода из цикла обрабатываем результаты
if ages:
    # Количество друзей
    print("Количество друзей:", len(names))
    
    # Средний возраст
    average_age = sum(ages) / len(ages)
    print("Средний возраст друзей:", round(average_age, 2))
    
    # Самый старший друг
    max_age = max(ages)
    oldest_friend_index = ages.index(max_age)
    oldest_friend = names[oldest_friend_index]
    print(f"Самый старший друг: {oldest_friend}, возраст: {max_age}")
else:
    print("Вы не ввели данные о друзьях.")