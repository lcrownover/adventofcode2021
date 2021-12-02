#!/usr/bin/env python3


def first(inputs):
    position, depth = 0, 0
    for command in inputs:
        x = int(command.split(" ")[1])
        if "forward" in command:
            position += x
        if "up" in command:
            depth -= x
        if "down" in command:
            depth += x
    return position * depth


def second(inputs):
    position, depth, aim = 0,0,0
    for command in inputs:
        x = int(command.split(" ")[1])
        if "forward" in command:
            position += x
            depth += aim * x
        if "up" in command:
            aim -= x
        if "down" in command:
            aim += x
    return position * depth



with open("inputs.txt", "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]

print(first(inputs))

print(second(inputs))
