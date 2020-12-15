import sys
import re

mask_ex = re.compile(r'^mask = ([01X]+)$')
mem_ex = re.compile(r'^mem\[(\d+)\] = (\d+)$')

mem = {}
# assume first line sets masks
or_mask = -1
and_mask = -1
with open(sys.argv[1]) as file:
    for line in file:
        if (line.startswith('mask')):
            mask = mask_ex.match(line).groups()[0]
            or_mask = int(mask.replace('X','0'), base=2)
            and_mask = int(mask.replace('X','1'), base=2)
            continue
        address, value = mem_ex.match(line).groups()
        value = (int(value) | or_mask) & and_mask
        mem[int(address)] = value
print(sum(mem.values()))
