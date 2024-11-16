# У вас есть два множества: одно содержит номера книг,
#  которые были выданы в библиотеке, а другое — номера книг, 
# которые вернули читатели.
# Найдите:
# Все книги, которые ещё не были возвращены (разность двух множеств).
# Все книги, которые были возвращены (пересечение двух множеств).
# Все книги, которые когда-либо были в библиотеке 
# (объединение двух множеств).
# Также найдите, какие книги были выданы, но не возвращены, 
# и какие книги вернули, но не были выданы.
# Условия:
# Множество выданных книг: {1, 2, 3, 4, 5, 6}
# Множество возвращенных книг: {2, 4, 6, 7}
# Попробуйте решить задачу, используя операторы для множеств:

# Разность (выданы, но не возвращены).
# Пересечение (возвращены).
# Объединение (все книги).


out_books = {1,2,3,4,5,6}
in_books = {2,4,6,7}

sub_books = out_books - in_books
passed_books = out_books & in_books
all_books = out_books | in_books
print(f"Books not library {sub_books}")
print(f"Books in library {passed_books}")
print(f"All books {all_books}")