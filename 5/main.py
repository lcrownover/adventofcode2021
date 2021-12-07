#!/usr/bin/env python3


def is_horizontal(x1, x2, y1, y2):
    if (x1 == x2) or (y1 == y2):
        return True
    return False


def expand_horizontal(x1, y1, x2, y2):
    out = []
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            out.append((x, y))
    return list(set(out))


def expand_diagonal(x1, y1, x2, y2):
    print(f"begin expand: {x1} {y1} {x2} {y2}")
    rev_x, rev_y = None, None
    if x1 > x2:
        x1, x2 = x2, x1
        rev_x = True
    if y1 > y2:
        y1, y2 = y2, y1
        rev_y = True
    xl = [i for i in range(x1, x2 + 1)]
    yl = [i for i in range(y1, y2 + 1)]
    if rev_x:
        xl = reversed(xl)
    if rev_y:
        yl = reversed(yl)
    return list(zip(xl, yl))


def first(inputs):
    main = {}
    for line in inputs:
        pair1, pair2 = line.split(" -> ")
        x1, y1 = pair1.split(",")
        x2, y2 = pair2.split(",")
        if not is_horizontal(x1, x2, y1, y2):
            continue
        for pair in expand_horizontal(int(x1), int(y1), int(x2), int(y2)):
            if pair in main:
                main[pair] += 1
            else:
                main[pair] = 1
    return sum([1 for v in main.values() if v >= 2])


def second(inputs):
    main = {}
    for line in inputs:
        print(f"processing line: {line}")
        pair1, pair2 = line.split(" -> ")
        x1, y1 = pair1.split(",")
        x2, y2 = pair2.split(",")
        if is_horizontal(x1, x2, y1, y2):
            pairs = expand_horizontal(int(x1), int(y1), int(x2), int(y2))
        else:
            pairs = expand_diagonal(int(x1), int(y1), int(x2), int(y2))
        for pair in pairs:
            print(f"pair processed: {pair}")
            if pair in main:
                main[pair] += 1
            else:
                main[pair] = 1
    return sum([1 for v in main.values() if v >= 2])


import sys

with open(sys.argv[1], "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]

# print(first(inputs))

print(second(inputs))

# test = 8, 0, 0, 8
# print(expand_diagonal(*test))
