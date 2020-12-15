import re
import sys

valid = 0
pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
with open(sys.argv[1]) as file:
    for line in file:
        start, stop, char, password = re.match(pattern, line).groups()
        start, stop = int(start), int(stop)
        count = 0
        count += (password[start-1] == char)
        count += (password[stop-1] == char)
        if count == 1:
            valid += 1
print(valid)