import sys

# quadratic; but input is only 200 items
terms = set()
sums = {}
with open(sys.argv[1]) as file:
    for line in file:
        n = int(line)
        if 2020 - n in sums:
            print(n * sums[2020 - n][0] * sums[2020 - n][1])
            break
        for n0 in terms:
            sums[n0 + n] = (n0, n)
        terms.add(n)
