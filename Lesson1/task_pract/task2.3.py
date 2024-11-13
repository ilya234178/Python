def circle_area(radius):
    S = 3.14159 * radius**2  # Используем ** для возведения в квадрат
    return S

num = float(input("Enter the radius: "))  # Преобразуем ввод в число с плавающей точкой
result = circle_area(num)
print(f"The area of the circle is: {result}")
