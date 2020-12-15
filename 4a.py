import sys

valid = 0
fields_seen = set()
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line == '':
            if len(fields_seen) == 8 or (len(fields_seen) == 7 and not 'cid' in fields_seen):
                valid += 1
            fields_seen.clear()
            continue
        pairs = line.split(' ')
        for pair in pairs:
            field, _ = pair.split(':')
            fields_seen.add(field)
if len(fields_seen) == 8 or (len(fields_seen) == 7 and not 'cid' in fields_seen):
    valid += 1
print(valid)