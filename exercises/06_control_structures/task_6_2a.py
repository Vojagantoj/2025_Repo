# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
add = input("Введите адрес: ")
ipadd = []
add = add.split(".")
if len(add) == 4 and ''.join(add).isdigit():
    for i in add:
        if i != "" and 0 <= int(i) <= 255:
            ipadd.append(int(i))
        else:
            print("Неправильный IP-адрес")
            break
else:
    print("Неправильный IP-адрес")
if len(ipadd) == 4 and 1 <= ipadd[0] <= 223:
        print('unicast')
elif len(ipadd) == 4 and 224 <= ipadd[0] <= 239 :
    print('multicast')
elif len(ipadd) == 4 and ipadd[0] == ipadd[1] == ipadd[2] == ipadd[3] == 255:
    print('local broadcast')
elif len(ipadd) == 4 and ipadd[0] == ipadd[1] == ipadd[2] == ipadd[3] == 0:
    print('unassigned')
elif len(ipadd) == 4:
    print('unused')