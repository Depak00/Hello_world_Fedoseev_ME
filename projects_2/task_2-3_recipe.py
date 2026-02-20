#!/bin/python
name = input("Введите название питательной среды: ")
conc = int(input("Введите концентрацию агара (%): "))
temp = int(input("Введите температуру стерилизации (°C): "))
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name}\n{conc}\t {temp}\n")
print("Файл 'recipe.txt' успешно сформирован!")
