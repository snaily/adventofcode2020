import sys

largest_id = -1
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        row = int(line[:7].replace('F','0').replace('B','1'), base=2)
        column = int(line[7:].replace('L','0').replace('R','1'), base=2)
        id_ = row * 8 + column
        if (id_ > largest_id):
            largest_id = id_
print(largest_id)
