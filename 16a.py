import re
import sys

field_ex = re.compile(r'^[^:]+: (\d+)-(\d+) or (\d+)-(\d+)$')

# [(low, high)]
ranges = []
scanrate = 0
with open(sys.argv[1]) as file:
    for line in file:
        if line == '\n':
            break
        alow, ahigh, blow, bhigh = field_ex.match(line).groups()
        ranges.append((int(alow), int(ahigh)))
        ranges.append((int(blow), int(bhigh)))

    for line in file:
        if line == 'nearby tickets:\n':
            break
    
    for line in file:
        values = [int(value) for value in line.strip().split(',')]
        for value in values:
            any_valid = False
            for low, high in ranges:
                if low <= value <= high:
                    any_valid = True
            if not any_valid:
                scanrate += value
print(scanrate)

    