import sys

def transform(n):
    n *= n
    n %= 20201227
    return n

solutions = []
with open(sys.argv[1]) as file:
    for line in file:
        N = int(line.strip())
        n = 1
        i = 0
        while n != N:
            i += 1
            n *= 7
            n %= 20201227
        solutions.append((N, i))

print(solutions)

k = solutions[0][0]
n = 1
for _ in range(solutions[1][1]):
    n *= k
    n %= 20201227
print(n)