#!/usr/bin/env python3


def first(inputs):
    g = []
    e = []
    for c in range(len(inputs[0])):
        x = 0
        for line in inputs:
            if line[c] == "1":
                x += 1
        if x > (len(inputs) / 2):
            g.append("1")
            e.append("0")
        else:
            g.append("0")
            e.append("1")
    gd = int("".join(g), 2)
    ed = int("".join(e), 2)
    return gd * ed


def second(inputs):
    ogr = [i for i in inputs]
    csr = [i for i in inputs]
    for c in range(len(inputs[0])):
        if len(ogr) == 1:
            break
        x = sum([1 for line in ogr if line[c] == "1"])
        if x >= (len(ogr) / 2):
            ogr = [i for i in ogr if list(i)[c] == "1"]
        else:
            ogr = [i for i in ogr if list(i)[c] == "0"]

    for c in range(len(inputs[0])):
        if len(csr) == 1:
            break
        x = sum([1 for line in csr if line[c] == "1"])
        if x >= (len(csr) / 2):
            csr = [i for i in csr if list(i)[c] == "0"]
        else:
            csr = [i for i in csr if list(i)[c] == "1"]

    ogrd = int("".join(ogr), 2)
    csrd = int("".join(csr), 2)
    return ogrd * csrd


with open("inputs.txt", "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]

print(first(inputs))

print(second(inputs))
