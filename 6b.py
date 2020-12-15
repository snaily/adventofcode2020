import sys

answers = {}
groupsize = 0
total = 0
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line == '':
            for count in answers.values():
                if count == groupsize:
                    total += 1
            answers.clear()
            groupsize = 0
            continue
        groupsize += 1
        for char in line:
            answers[char] = answers.get(char, 0) + 1
print(total)