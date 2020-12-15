import sys

seen_ids = [0] * (828+1) # 828 is the known largest id
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        row = int(line[:7].replace('F','0').replace('B','1'), base=2)
        column = int(line[7:].replace('L','0').replace('R','1'), base=2)
        id_ = row * 8 + column
        seen_ids[id_] = 1
i = 0
while seen_ids[i] == 0:
    i += 1
while seen_ids[i] == 1:
    i += 1
print(i)
