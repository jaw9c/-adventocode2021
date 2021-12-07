#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = ["3,4,3,1,2"]

def clean_input(input):
    return list(map(int, input[0].split(",")))


def init(input):
    return {
        i: len(list(filter(lambda x: x==i, input))) for i in range(9)
    }

def step(popualtion):
    pop0 = popualtion[0]
    new_pop = {
        i: popualtion[i+1] for i in range(8)
    }
    new_pop[8] = pop0
    new_pop[6] = new_pop[6] + pop0
    return new_pop


def doit(input):
    for _ in range(256):
        input = step(input)
    return sum(input.values())


if __name__ == "__main__":
    print(doit(init(clean_input(input))))
