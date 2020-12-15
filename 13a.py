import sys

time = -1
buses = []
with open(sys.argv[1]) as file:
    time = int(file.readline())
    buses = [int(bus) for bus in file.readline().split(',') if not bus == 'x']
print(time, buses)

done = False
for wait in range(max(buses)):
    for bus in buses:
        if time % bus == 0:
            print(wait * bus)
            done = True
            break
    if done:
        break
    time += 1