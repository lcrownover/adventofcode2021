#!/usr/bin/env python3


def expand(x1, y1, x2, y2):
    print(f"begin expand: {x1} {y1} {x2} {y2}")
    out = []
    for x in range(x1, x2):
        for y in range(y1, y2):
            print(f"appending: ({x}, {y})")
            out.append((x, y))
    print(out)
    print(f"end expand: {x1} {y1} {x2} {y2}")
    return list(set(out))


def first(inputs):
    main = {}
    for line in inputs:
        print(f"processing line: {line}")
        pair1, pair2 = line.split(" -> ")
        x1, y1 = pair1.split(",")
        x2, y2 = pair2.split(",")
        for pair in expand(int(x1), int(y1), int(x2), int(y2)):
            print(f"pair processed: {pair}")
            if pair in main:
                main[pair] += 1
            else:
                main[pair] = 1
    c = 0
    for k, v in main.items():
        if v >= 2:
            c += 1
    return c


def second(inputs):
    pass


import sys
with open(sys.argv[1], "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]

print(first(inputs))

print(second(inputs))
