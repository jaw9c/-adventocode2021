#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def clean_input(input):
    return [(cmd, int(val)) for (cmd, val) in [x.split(" ") for x in input]]

def doit(input):
    pos = (0, 0) # (depth, horizontal)

    for (cmd, val) in clean_input(input):
        if cmd == "forward":
            pos = (pos[0], pos[1] + val)
        if cmd == "down":
            pos = (pos[0] + val, pos[1])
        if cmd == "up":
            pos = (pos[0] - val, pos[1])
    
    return pos[0] * pos[1]

if __name__ == "__main__":
    print(doit(input))
