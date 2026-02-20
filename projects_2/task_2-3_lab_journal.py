#!/bin/python
with open("journal.txt", "w") as journal:
    journal.write("")

name = input("ФИО исследователя : ")
date = input("Дата: ")
eksp = input("Эксперимент: ")
out = input("Вывод: ")

dname = 51 - len(name) - len("| Имя: ")- 2
dspace = 51 - len(date) - len("| Дата: ")- 2
deskp = 51 - len(eksp) - len("| Эксперимент: ") - 2

s=""
words = out.split(" ")
with open("journal.txt", "a") as journal:
    journal.write("+--------------------------------------------------+\n")
    journal.write("| Электронный журнал                               |\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write(f"| Имя: {name} {dname*" "} | \n")
    journal.write(f"| Дата: {date} {dspace*" "} |\n")
    journal.write(f"| Эксперимент: {eksp} {deskp*" "} |\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write("| Вывод:                                           |\n")
    journal.write("|")
    for w in range(len(words)):
        if len(s) + len(words[w]) > 35:
            s+=" "
            s+=words[w]
            ds = 51 - len(s) - 2
            journal.write(f"{s} {ds*" "}|\n")
            s=""
            journal.write("|")
        else:
            s+=" "
            s+=words[w]
    ds = 51 - len(s) - 2
    journal.write(f"{s} {ds*" "}|\n")
    journal.write("+--------------------------------------------------+")
