n = int(input("Number: "))
for i in range(1 , n):
    if i % 3 == 0:
        continue
    else:
        print(i)