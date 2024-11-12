friend1 = input("Напиши свое имя: ")
age1 = int(input("Какой твой возраст?"))
friend2 = input("Напиши свое имя: ")
age2 = int(input("Какой твой возраст?"))
friend3 = input("Напиши свое имя: ")
age3 = int(input("Какой твой возраст?"))

average_age = round((age1 + age2 + age3) / 3, 2)
print(f"Средний возраст {friend1}, {friend2} и {friend3} равен {average_age} лет")
