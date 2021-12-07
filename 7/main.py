def first(nums):
    s = list(sorted(nums))
    target = (s[len(s) // 2])
    return sum(map(lambda x: abs(x - target), nums))

def second(nums):
    pass


import sys

with open(sys.argv[1], "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]
    nums = [int(n) for n in inputs[0].split(',')]

print(first(nums))

# print(second(nums))
