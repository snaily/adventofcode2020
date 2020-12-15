import sys
import math

time = -1
buses = []
with open(sys.argv[1]) as file:
    _ = int(file.readline())
    buses = file.readline().split(',')
print(buses)

total_period = 1
time = 0
for offset, period in enumerate(buses):
    if period == 'x':
        continue
    period = int(period)
    while (time + offset) % period != 0:
        time += total_period
    total_period *= period
    print(time, total_period)
print(time)