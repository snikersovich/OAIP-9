#Задача 1
a = input("Введите число: ")
b = input("Введите второе число: ")
try:
    a = int(a)
    b = int(b)
    result = int(a) + int(b)
    print('Сумма ваших чисел:', result)
except ValueError:
    print("Поддерживаются только числа!")

#Задача 2
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    try:
        result = int(a)+int(b)
    except ValueError:
        print("Поддерживаются только числа!")
    except ZeroDivisionError:
        print("Сумма ваших чисел:")
    else:
        print(result)
        break

#Задача 3
a = input("Введите первый делитель: ")
b = input("Введите второй делитель: ")
try:
    a = int(a)
    b = int(b)
    result = int(a) / int(b)
    print('Частное ваших чисел:', result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")

#Задача 4
a = input("Введите число: ")
b = input("Введите второе число: ")
try:
    a = int(a)
    b = int(b)
    result = int(a) + int(b)
    result2 = int(a) / int(b)
    print('Сумма ваших чисел:', result)
except (ValueError, ZeroDivisionError):
    print("Ошибка")
else:
    print(result2)

#Задача 5
a = input("Введите число: ")
b = input("Введите второе число: ")
try:
    a = int(a)
    b = int(b)
    result = int(a) + int(b)
    result2 = int(a) / int(b)
    print('Сумма ваших чисел:', result)
except (ValueError, ZeroDivisionError):
    print("Ошибка")
else:
    print(result2)
finally:
    print('Выход из программы')

