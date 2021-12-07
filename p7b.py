#!/usr/bin/python3
from utils import *
import math

input = load_input_as_list()

test_input = ["16,1,2,0,4,2,7,1,2,14"]

def clean_input(input):
    return list(map(int, input[0].split(",")))

def sum_of_nat(n):
    return (n * (n+1)) / 2

def doit(input):
    min = math.inf
    for pos in range(max(input)):
        fuel = sum([sum_of_nat(pos - x) if x < pos else sum_of_nat(x - pos) for x in input])
        if fuel < min:
            min = fuel
    return min

if __name__ == "__main__":
    print(doit(clean_input(input)))
