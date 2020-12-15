import sys

state = {
    'acc': 0,
    'pc': 0,
}

def nop(state, argument):
    state['pc'] += 1
    return state
def acc(state, argument):
    state['acc'] += argument
    state['pc'] += 1
    return state
def jmp(state, argument):
    state['pc'] += argument
    return state
instructions = {
    'nop': nop,
    'acc': acc,
    'jmp': jmp,
}

program = []
with open(sys.argv[1]) as file:
    for line in file:
        instruction, argument = line.strip().split(' ')
        program.append((instruction, int(argument)))

executed = [False] * len(program)
while not executed[state['pc']]:
    executed[state['pc']] = True
    instruction, argument = program[state['pc']]
    state = instructions[instruction](state, argument)

print(state['acc'])
