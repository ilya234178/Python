# Однако ты можешь создать новый кортеж с нужными изменениями:
my_tuple = (1, 2, 3, 4, 5, 6)
new_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print(new_tuple)  # Выведет: (1, 2, 10, 4, 5, 6)