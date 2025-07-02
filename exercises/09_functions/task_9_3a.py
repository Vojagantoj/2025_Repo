# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    '''Создаем карту интерфейс - вланы'''
    with open(config_filename, 'r') as f:
        access = dict()
        trunk = dict()
        result = []
        for line in f:
            if line.startswith('interface '):
                inter = line.split()[-1]
                continue
            elif 'switchport mode access' in line:
                access[inter] = int('1')
            elif 'access vlan' in line:
                access[inter] = int(line.split()[-1])
                continue
            elif 'trunk allowed' in line:
                vlans = line.split()[-1]
                doom = []
                for i in vlans.split(','):
                    doom.append(int(i))
                    trunk[inter] = doom
    result.append(access)
    result.append(trunk)
    result = tuple(result)
    return result