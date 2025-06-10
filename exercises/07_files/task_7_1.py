# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vault = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
with open('ospf.txt') as f:
    for line in f:
        j = 0
        i = 1
        line_list = line.split()
        while i <= 6 and j <= 4:
            if line_list[i].strip('[]') == 'via':
                i += 1
                pass
            elif i == 5 or i == 4:
                a = vault[j]
                b = line_list[i].rstrip(',')
                j += 1
                i += 1
                print('{:<21}    {}'.format(a, b))
                pass
            else:
                k = vault[j]
                z = line_list[i].strip('[]')
                j += 1
                i += 1
                print('{:<21}    {}'.format(k, z))
