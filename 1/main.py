#!/usr/bin/env python3

with open('inputs.txt', 'r') as f:
    entries = [int(line.strip()) for line in f.readlines() if line.strip()]


def second(entries):
    count = 0
    for i,_ in enumerate(entries):
        if i == 0:
            continue
        if i+3 > len(entries):
            return count
        if sum(entries[i:i+3]) > sum(entries[i-1:i+2]):
            count += 1

ans = second(entries)
print(ans)

