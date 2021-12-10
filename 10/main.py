def process(line) -> str:
    key = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    expected = []
    stack = []
    queue = list(line)
    for c in queue:
        if c in key.keys():
            expected.append(key[c])
            stack.append(c)
        if c in key.values():
            if c != expected[-1]:
                return c
            stack.pop()
            expected.pop()
    return ""

def process2(line) -> int:
    key = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    expected = []
    stack = []
    queue = list(line)
    for c in queue:
        if c in key.keys():
            expected.append(key[c])
            stack.append(c)
        if c in key.values():
            if c != expected[-1]:
                return 0
            stack.pop()
            expected.pop()
    total = 0
    for c in reversed(expected):
        total *= 5
        total += score[c]
    return total

def vals(c: str) -> int:
    vals = {
        "": 0,
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return vals[c]


def first(lines):
    val = 0
    for line in lines:
        bad = process(line)
        val += vals(bad)
    return val



def second(lines):
    scores = []
    for i,line in enumerate(lines):
        score = process2(line)
        if score == 0:
            continue
        scores.append(score)
    m_i = int(((len(scores)-1)/2))
    return sorted(scores)[m_i]


import sys

# f = "10/test_inputs.txt"
f = "10/inputs.txt"
with open(f, "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# print(first(lines))

print(second(lines))
