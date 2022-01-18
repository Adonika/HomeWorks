# Создать 4 переменных разных типов и указать в них данные.
# Например: color, age, animal, alcohol и так далее.
# С использованием данных переменных написать программу, которая выводит текст

color = input("Введите цвет питомца: ")
animal = input("Введите вид питомца: ")
print(f"Ваши питомец {animal}, его цвет {color}.")

age = int(input("Ваш возраст: "))
alcohol = 18
if age < 18:
    print("Вы несовершеннолетний!")
elif age > 135:
    print("Ошибка в возрасте!")
else:
    print("Вы уже взрослый!")

num1 = float(input("Введите число №1: "))
num2 = float(input("Введите число №2: "))
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Zero division")
