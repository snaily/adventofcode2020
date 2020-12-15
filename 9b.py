import sys
import collections

target = 144381670 # known from part 1
nums = collections.deque()
sum = 0
with open(sys.argv[1]) as file:
    for line in file:
        while sum > target:
            sum -= nums.popleft()
            if sum == target:
                print(min(nums) + max(nums))
                break
        num = int(line)
        nums.append(num)
        sum += num
        if sum == target:
            print(min(nums) + max(nums))
            break