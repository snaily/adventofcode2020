import sys

with open(sys.argv[1]) as file:
    for line in file:
        nums = [int(num) for num in line.split(',')]
        last = nums.pop()
        ages = {num: i for i, num in enumerate(nums)}
        for i in range (len(nums), 2020):
            age = ages.get(last, -1)
            nums.append(last)
            ages[last] = i
            if age == -1:
                last = 0
            else:
                last = i - age
        print(nums[-1])
