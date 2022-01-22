# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне по следующему правилу:
# если число кратно 7, его надо выводить на экран.

# a = int(input("Enter the start number of the range: "))
# b = int(input("Enter the end number of the range: "))
# if a < b:
#     if a > 0 and b > 0:
#         while a <= b:
#             if a % 7 == 0:
#                 print(a, end=' ')
#             a = a + 1
#     else:
#         print("Error in start number")
# else:
#     print("Error in range")

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне.
# Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

# a = int(input("Enter the start number of the range: "))
# b = int(input("Enter the end number of the range: "))
# c = int(input("Select option(1, 2, 3, 4): "))
# if c == 1:
#     if a < b:
#         if a >= 0 and b >= 0:
#             while a <= b:
#                 print(a, end=' ')
#                 a = a + 1
#         else:
#             print("Error in start number")
#     else:
#         print("Error in range")
# elif c == 2:
#     if a < b:
#         if a >= 0 and b >= 0:
#             while b >= a:
#                 print(b, end=' ')
#                 b = b - 1
#         else:
#             print("Error in start number")
#     else:
#         print("Error in range")
# elif c == 3:
#     if a < b:
#         if a > 0 and b > 0:
#             while a <= b:
#                 if a % 7 == 0:
#                     print(a, end=' ')
#                 a = a + 1
#         else:
#             print("Error in start number")
#     else:
#         print("Error in range")
# elif c == 4:
#     if a < b:
#         if a > 0 and b > 0:
#             d = 0
#             while a <= b:
#                 if a % 5 == 0:
#                     d = d + 1
#                 a = a + 1
#             print(d)
#         else:
#             print("Error in start number")
#     else:
#         print("Error in range")
# else:
#     print("Error in option")

# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне.
# Вывод на экран должен проходить по правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.

# a = int(input("Enter the start number of the range: "))
# b = int(input("Enter the end number of the range: "))
# if a < b:
#     if a > 0 and b > 0:
#         while a <= b:
#             if a % 3 == 0 and a % 5 == 0:
#                 print(f"{a} Fizz Buzz")
#             elif a % 3 == 0:
#                 print(f"{a} Fizz")
#             elif a % 5 == 0:
#                 print(f"{a} Buzz")
#             elif a % 3 != 0 and a % 5 != 0:
#                 print(a)
#             a = a + 1
#     else:
#         print("Error in start number")
# else:
#     print("Error in range")

