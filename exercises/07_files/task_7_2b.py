# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


from sys import argv
file = argv[1]
end_file = argv[2]
ign = set(ignore)
with open(file) as src, open(end_file, 'w') as dest:
    for line in src:
        lines = set(line.split())
        if ign.intersection(lines) or line.startswith('!'):
            continue
        else:
            dest.write(line)