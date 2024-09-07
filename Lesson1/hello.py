#типы данных и переменная
# int,float,boolean,str,list,None

# value = None
# a = 123
# b = 1.23
#print(type(a))
#print(type(b))
#value = 12453
# #print(type(value))
# s = 'hello world'
# print(s)
# print(a,b,s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')


# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['hello',1,2,3,True]
# print(list)
# print(col)


# print('введите a : ')
# a = int(input())
# print('введите b :')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)
# print(f'{a} {b}')

# a = 1.3342
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5
# print(a)

# a = 1 < 3 and 5 > 2
# print(a)
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2 
# print(is_odd)


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это Маша')
# elif username == 'Марина':
#     print('Hello, Marina')
# else:
#     print('hello, ' + username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('пожалуй')
#     print('хватит')
# print(inverted)


# for i in range(1, 10, 2):
#     print(i)

# text = 'съешь еще этих мягких французских булок'

# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ' ))

# for c in text:
#     print(c)

# numbers = [1,2,3,4]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

def f(x):
    if x ==1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
    
arg = 1
print(f(arg))
print(type(f(arg)))