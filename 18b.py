import sys

def apply_op(stack, op):
    if op == '*':
        stack.append(stack.pop() * stack.pop())
    if op == '+':
        stack.append(stack.pop() + stack.pop())

def shunting_yard_with_eval(tokens):
    stack = []
    ops = []
    for token in tokens:
        if token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                apply_op(stack, ops.pop())
            ops.pop()
        elif token == '*':
            while ops and (ops[-1] == '*' or ops[-1] == '+'):
                apply_op(stack, ops.pop())
            ops.append(token)
        elif token == '+':
            while ops and ops[-1] == '+':
                apply_op(stack, ops.pop())
            ops.append(token)
        else:
            stack.append(int(token))
    while ops:
        apply_op(stack, ops.pop())
    assert len(stack) == 1
    return stack[0]

total = 0
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip().replace(' ','')
        result = shunting_yard_with_eval(line)
        print(result)
        total += result
print(total)
