def first(nums):
    s = list(sorted(nums))
    target = (s[len(s) // 2])
    return sum(map(lambda x: abs(x - target), nums))

def exp(n):
    return sum([n for n in range(1, n+1)])

def second(nums):
    s = list(sorted(nums))
    target = int(sum(s) / len(s))
    return sum(map(lambda x: exp(abs(x - target)), nums))


import sys

with open(sys.argv[1], "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]
    nums = [int(n) for n in inputs[0].split(',')]

print(first(nums))

print(second(nums))
