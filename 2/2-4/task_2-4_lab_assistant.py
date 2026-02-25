#!/bin/python
o = float(input("Введите нужный объем раствора (в мл): "))

with open("recipe.txt", "w", encoding='utf-8') as recipe:
    recipe.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n{23*'-'}\nОбщий объем: {o} мл\nМасса соли: {(0.009*o):.2f}\nОбъем воды: {o}")
