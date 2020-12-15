import re
import sys

valid = 0
pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
with open(sys.argv[1]) as file:
    for line in file:
        min_, max_, char, password = re.match(pattern, line).groups()
        min_, max_ = int(min_), int(max_)
        count = password.count(char)
        if min_ <= count <= max_:
            valid += 1
print(valid)