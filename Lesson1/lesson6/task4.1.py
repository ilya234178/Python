# Задача 1: Создайте словарь, который содержит информацию о книге: 
# название, автор, год издания. 
# Напечатайте все элементы словаря с помощью цикла.

book_info = {"author": "Tolstoy", "title": "War and Peace", "year": 1867}
print(book_info)
print(book_info["author"])
book_info["genre"] = "historical"
print(book_info)
removed_info = book_info.pop("year")
print(book_info)
print(removed_info)
if "author" in book_info:
    print("Yes")
else:
    print("No")