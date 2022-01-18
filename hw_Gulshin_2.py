# Домашнее задание 2
# Создать программу которая при вводе данных в переменную метр преобразует его в фут, дюйм, милю и
# литр в пинту, галлон, баррель.

metr = int(input("Введите количество метров: "))
foot = metr*3.28
dulm = metr*39.4
mile = metr/1609.34
print(f"В {metr} метрах:\n{foot} футов\n{dulm} дюльмов\n{mile} миль")
print("\n")
litr = float(input("Введите количество литров: "))
pint = litr*2.11
gallon = litr/3.785
barrel = litr*159
print(f"В {litr} литрах:\n{pint} пинт\n{gallon} галлонов\n{barrel} баррелей")

