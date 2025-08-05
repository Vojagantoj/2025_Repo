def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    command_output = command_output.split('\n')
    list = []
    result = {}
    a = False
    for line in command_output:
        if 'neighbors' in line:
            key = line[:line.find('>')]
        elif 'Device ID' in line:
            a = True
            continue
        elif a and line:
            list.append(line)
    for rout in list:
        ro = rout.split()[0]
        int_loc = rout.split()[1]+rout.split()[2]
        int_rem = rout.split()[-2]+rout.split()[-1]
        keys = tuple([key, int_loc])
        values = tuple([ro, int_rem])
        result[keys] = values
    return result





