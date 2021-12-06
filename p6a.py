#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = ["3,4,3,1,2"]

def clean_input(input):
    return list(map(int, input[0].split(",")))



def step(input):
    return [x-1 for x in input if x > 0] + flatten([[6, 8] for x in input if x == 0])


def doit(input):
    for _ in range(80):
        input = step(input)
    return input


if __name__ == "__main__":
    print(len(doit(clean_input(input))))
