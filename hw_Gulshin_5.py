# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.
# Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.
#
num = int(input("Enter number: "))
if (num >= 1) and (num <= 100):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 != 0 and num % 5 != 0:
        print(num)
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
else:
    print("Error")

# Задание 2
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.

num = int(input("Enter number: "))
count = 0
while count <= 7:
    print(f"{num} ** {count} = {num ** count}")
    count = count + 1

# Задание 3
# Написать программу подсчета стоимости разговора для разных мобильных операторов.
# Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит.
# Вывести стоимость на экран.

cost1 = float(input("Enter cost for life: "))
cost2 = float(input("Enter cost for vodaphone: "))
oper1 = str(input("Enter your operator(life, vodaphone): "))
oper2 = str(input("Enter your friends operator(life, vodaphone): "))
time = int(input("Enter time in min: "))
if oper1 == 'life' and oper2 == 'life':
    print(f"Cost for {time} min from {oper1} to {oper2} will be {(cost1 * time) * 1}")
elif oper1 == 'life' and oper2 == 'vodaphone':
    print(f"Cost for {time} min from {oper1} to {oper2} will be {(cost1 * time) * 3}")
elif oper1 == 'vodaphone' and oper2 == 'vodaphone':
    print(f"Cost for {time} min from {oper1} to {oper2} will be {(cost2 * time) * 1}")
elif oper1 == 'vodaphone' and oper2 == 'life':
    print(f"Cost for {time} min from {oper1} to {oper2} will be {(cost2 * time) * 2}")
else:
    print("Error")

# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры уровень продаж для трех менеджеров.
# Определить их зарплату, определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.

sale1 = int(input("Enter sales for 1 manager: "))
sale2 = int(input("Enter sales for 2 manager: "))
sale3 = int(input("Enter sales for 3 manager: "))
if sale1 >= 0:
    if sale1 == 0:
        print("Manager 1 is bad worker")
    elif (sale1 >= 500) and (sale1 <= 1000):
        print(f"Salary for manager 1 is {200 + (sale1 * 0.05)}")
    elif sale1 < 500:
        print(f"Salary for manager 1 is {200 + (sale1 * 0.03)}")
else:
    print("Error in sale level for manager 1")
if sale2 >= 0:
    if sale2 == 0:
        print("Manager 2 is bad worker")
    elif (sale2 >= 500) and (sale2 <= 1000):
        print(f"Salary for manager 2 is {200 + (sale2 * 0.05)}")
    elif sale2 < 500:
        print(f"Salary for manager 2 is {200 + (sale2 * 0.03)}")
else:
    print("Error in sale level for manager 2")
if sale3 >= 0:
    if sale3 == 0:
        print("Manager 3 is bad worker")
    elif (sale3 >= 500) and (sale3 <= 1000):
        print(f"Salary for manager 3 is {200 + (sale3 * 0.05)}")
    elif sale3 < 500:
        print(f"Salary for manager 3 is {200 + (sale3 * 0.03)}")
else:
    print("Error in sale level for manager 3")
