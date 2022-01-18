# Задание 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
command = str(input("Enter command + or *: "))
if command == '+':
    print(f"{num1} + {num2} + {num3} = {num1+num2+num3}")
elif command == '*':
    print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")
else:
    print("Error")

# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
command = str(input("Enter command min or max or average: "))
if command == 'max':
    if num1 > num2 and num1 > num3:
        print("num1 ", num1)
        if num2 > num3:
            print(num2)
            print(num3)
        else:
            print(num3)
            print(num2)
    elif num2 > num1 and num2 > num3:
        print("num2 ", num2)
        if num1 > num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
    elif num3 > num2 and num3 > num1:
        print("num3", num3)
        if num1 > num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)
    else:
        print("Error")
elif command == 'min':
    if num1 < num2 and num1 < num3:
        print("num1 ", num1)
        if num2 < num3:
            print(num2)
            print(num3)
        else:
            print(num3)
            print(num2)
    elif num2 < num1 and num2 < num3:
        print("num2 ", num2)
        if num1 < num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
    elif num3 < num2 and num3 < num1:
        print("num3", num3)
        if num1 < num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)
    else:
        print("Error")
elif command == 'average':
    print(f"({num1}+{num2}+{num3})/3 = {(num1+num2+num3)/3}")
else:
    print("Error")

# Задание 3
# Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.

meter = float(input("Enter meters: "))
typ = str(input("Enter your type of distance miles, inches, yards: "))
if typ == 'miles':
    print(f"In {meter} meters {meter/1609.34} miles.")
elif typ == 'inches':
    print(f"In {meter} meters {meter*39.4} inches.")
elif typ == 'yards':
    print(f"In {meter} meters {meter*1.094} yards.")
else:
    print("Error")
