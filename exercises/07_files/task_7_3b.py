# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
g = input('Введите номер влана: ')
fix = []
i = 0
with open('CAM_table.txt') as f:
    for line in f:
        lines = line.split()
        if line == '\n':
            continue
        elif lines[0].isdigit():
            lines.insert(0, int(lines[0]))
            lines.pop(1)
            lines.remove('DYNAMIC')
            fix += [lines]
        else:
            continue
    for i in range (len(fix)):
        if int(g) != fix[i][0]:
            continue
        else:
            vlan, mac, intf = fix[i]
            print("{:<9} {:<16} {:>11}".format(vlan, mac, intf))