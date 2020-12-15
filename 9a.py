import sys
import collections

preamble = int(sys.argv[2])
nums = collections.deque(maxlen=preamble)
with open(sys.argv[1]) as file:
    for i, line in enumerate(file):
        num = int(line)
        if i >= preamble:
            found = False
            for j in range(preamble):
                for k in range(j):
                    if nums[j] + nums[k] == num:
                        found = True
                        break
            if not found:
                print(num)
                break
        nums.append(num)