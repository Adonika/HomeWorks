# Задание 1
# Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник,2 — вторник и т.д.

day_week = int(input("Enter your day of week: "))
if day_week == 1:
    print(f"Your day of the week is Monday")
elif day_week == 2:
    print(f"Your day of the week is Tuesday")
elif day_week == 3:
    print(f"Your day of the week is Wednesday")
elif day_week == 4:
    print(f"Your day of the week is Thursday")
elif day_week == 5:
    print(f"Your day of the week is Friday")
elif day_week == 6:
    print(f"Your day of the week is Saturday")
elif day_week == 7:
    print(f"Your day of the week is Sunday")
else:
    print("Error")

# Задание 2
# Пользователь вводит с клавиатуры номер месяца (1-12).
# Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

month = int(input("Enter your number of month: "))
if month == 1:
    print(f"Your month is January")
elif month == 2:
    print(f"Your month is February")
elif month == 3:
    print(f"Your month is March")
elif month == 4:
    print(f"Your month is April")
elif month == 5:
    print(f"Your month is May")
elif month == 6:
    print(f"Your month is June")
elif month == 7:
    print(f"Your month is July")
elif month == 8:
    print(f"Your month is August")
elif month == 9:
    print(f"Your month is September")
elif month == 10:
    print(f"Your month is October")
elif month == 11:
    print(f"Your month is November")
elif month == 12:
    print(f"Your month is December")
else:
    print("Error")

# Задание 3
# Пользователь вводит с клавиатуры число.
# Если число больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»

num = int(input("Enter your number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

# Задание 4
# Пользователь вводит два числа.
# Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке возрастания.

num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))
if num1 == num2:
    print("number 1 = number 2")
elif num1 > num2:
    print(f"{num2}, {num1}")
elif num1 < num2:
    print(f"{num1}, {num2}")
else:
    print("Error")
