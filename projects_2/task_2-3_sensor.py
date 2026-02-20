#!/bin/python
name = input("Введите имя оператора: ")
pres = int(input("Введите текущее значение давления (Па): "))
with open("sensor_log.txt", "a", encoding="utf-8") as sens:
    sens.write(f"{name}\t{pres}\n")
print("Данные успешно сохранены в sensor_log.txt")
