import sys

def add(a):
    return lambda b: a+b
def prod(a):
    return lambda b: a*b
ops = {
    '+': add,
    '*': prod
}
# parse a number or parenthesis and a subsequent operation
def eval(tokens):
    op = add(0)
    while True:
        token = tokens.pop()
        result = None
        if token == '(':
            sub_result, tokens = eval(tokens)
            result = op(sub_result)
        else:
            # token is a number
            result = op(int(token))

        if not tokens:
            return result, tokens
        next = tokens.pop()
        if next == ')':
            return result, tokens
        else:
            op = ops[next](result)

total = 0
with open(sys.argv[1]) as file:
    for line in file:
        # I can create my own precedence rules! With parentheses!
        line = line.strip().replace(' ', '')
        line = '((' + line.replace('(','(((')
        line = line.replace(')',')))') + '))'
        line = line.replace('*','))*((')
        line = line.replace('+',')+(')
        result, _ = eval(list(line)[::-1])
        total += result
print(total)
