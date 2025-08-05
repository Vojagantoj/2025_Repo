command_output = []
result = dict()
with open("sh_cdp_n_sw1.txt") as f:
    for line in f:
        command_output.append(line)
for i in command_output:
    if i.find('show cdp neighbors') > 0:
        name_device = i[:i.find('>')]
    elif i.startswith('R') or i.startswith('SW') and i.count('cdp neighbors') != 1:
        outp = i.split()
        key = [name_device, outp[1]]
        value = [outp[0], outp[-1]]
        result = dict()
print(result)