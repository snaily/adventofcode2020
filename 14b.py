import sys
import re

mask_ex = re.compile(r'^mask = ([01X]+)$')
mem_ex = re.compile(r'^mem\[(\d+)\] = (\d+)$')

def op(mask, address):
    if mask == '0':
        return address
    return mask

def apply(mask, address):
    return [op(m, v) for m, v in zip(mask, format(address, '0>36b'))]

mem = {}
with open(sys.argv[1]) as file:
    for line in file:
        if (line.startswith('mask')):
            mask = mask_ex.match(line).groups()[0]
            continue
        address, value = mem_ex.match(line).groups()
        address = apply(mask, int(address))
        xs = address.count('X')
        for i in range(2 ** xs):
            bits = format(i, f'0>{xs}b')
            k = 0
            actual_address = list(address)
            for j, c in enumerate(address):
                if c == 'X':
                    actual_address[j] = bits[k]
                    k += 1
            mem[int(''.join(actual_address), base=2)] = int(value)
print(sum(mem.values()))