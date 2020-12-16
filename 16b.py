import re
import sys

field_ex = re.compile(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')

# [(name, alow, ahigh, blow, bhigh, set(impossible indexes))]
fields = []
tickets = []
own_ticket = None
with open(sys.argv[1]) as file:
    for line in file:
        if line == '\n':
            break
        name, alow, ahigh, blow, bhigh = field_ex.match(line).groups()
        fields.append((name, int(alow), int(ahigh), int(blow), int(bhigh), set()))

    for line in file:
        if ',' in line:
            own_ticket = [int(value) for value in line.strip().split(',')]
        if line == 'nearby tickets:\n':
            break
    
    for line in file:
        values = [int(value) for value in line.strip().split(',')]
        all_valid = True
        for value in values:
            any_range = False
            for _, alow, ahigh, blow, bhigh, _ in fields:
                if alow <= value <= ahigh or blow <= value <= bhigh:
                    any_range = True
            if not any_range:
                all_valid = False
        if (all_valid):
            tickets.append(values)

# disqualify mappings
for ticket in tickets:
    for i, value in enumerate(ticket):
        for name, alow, ahigh, blow, bhigh, impossible_indexes in fields:
            if not (alow <= value <= ahigh or blow <= value <= bhigh):
                impossible_indexes.add(i)

# nicer data structure for mapping
mappings = {}
for name, _, _, _, _, impossible_indexes in fields:
    mappings[name] = set(range(len(tickets[0]))) - impossible_indexes

# dfs for assignment
def assign(mappings):
    if len(mappings) == 0:
        return mappings
    assign_name = ''
    shortest_length = len(tickets[0]) + 1
    print(mappings)
    for name, indexes in mappings.items():
        if len(indexes) < shortest_length:
            assign_name = name
            shortest_length = len(indexes)

    for index in mappings[assign_name]:
        new_mappings = {}
        for name, indexes in mappings.items():
            if name == assign_name:
                continue
            new_mappings[name] = indexes - set((index,))
        result_mappings = assign(new_mappings)
        if result_mappings != None:
            result_mappings[assign_name] = set((index,))
            return result_mappings
    return None

# generate result
product = 1
for name, indexes in assign(mappings).items():
    if name.startswith('departure'):
        product *= own_ticket[list(indexes)[0]]

print(product)