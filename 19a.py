import sys
import re

def char(c):
    assert len(c) == 1
    def parse(input):
        if input[0] == c:
            return input[1:]
    return parse
def sequence(parsers, indices):
    def parse(input):
        for parser in [parsers[i] for i in indices]:
            remain = parser(input)
            if remain != None:
                input = remain
            else:
                return None
        return input
    return parse
def alternate(parsers, sequences):
    sequences = [sequence(parsers, indices) for indices in sequences]
    def parse(input):
        for parser in sequences:
            remain = parser(input)
            if remain != None:
                return remain
        return None
    return parse


total = 0
with open(sys.argv[1]) as file:
    parsers = {}
    for line in file:
        line = line.strip()
        if line == '':
            break

        index, rule = line.split(':')
        index = int(index.strip())
        rule = rule.strip()
        if '"' in rule:
            parsers[index] = char(rule[1:-1])
        elif '|' in rule:
            parsers[index] = alternate(parsers, [[int(index) for index in alt.strip().split(' ')] for alt in rule.split('|')])
        else:
            parsers[index] = sequence(parsers, [int(index) for index in rule.split(' ')])
    
    for line in file:
        line = line.strip()
        remain = parsers[0](line)
        print (line, remain)
        if remain != None and len(remain) == 0:
            total += 1
print(total)
