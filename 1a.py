import sys

complement = set()
with open(sys.argv[1]) as file:
    for line in file:
        n = int(line)
        if n in complement:
            print(n*(2020-n))
            break
        complement.add(2020 - n)
