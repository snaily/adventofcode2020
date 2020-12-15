import sys

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

def exec(program):
    state = {
        'acc': 0,
        'pc': 0,
    }
    executed = [False] * len(program)
    while True:
        if state['pc'] == len(program):
            return (True, state['acc'])
        if (executed[state['pc']]):
            return (False, None)
        executed[state['pc']] = True
        instruction, argument = program[state['pc']]
        state = instructions[instruction](state, argument)

for i in range(len(program)):
    instruction, argument = program[i]
    if instruction == 'nop':
        program[i] = ('jmp', argument)
        completed, acc = exec(program)
        if (completed):
            print(acc)
            break
        program[i] = ('nop', argument)
    if instruction == 'jmp':
        program[i] = ('nop', argument)
        completed, acc = exec(program)
        if (completed):
            print(acc)
            break
        program[i] = ('jmp', argument)
