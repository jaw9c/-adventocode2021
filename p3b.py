#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def most_common(index, input):
    count = sum(1 if line[index] == "1" else -1 for line in input)
    return  "1" if count >= 0 else "0"

def least_common(index, input):
    count = sum(1 if line[index] == "1" else -1 for line in input)
    return  "1" if count < 0 else "0"

def doit(input):
    if len(input) == 1:
        return input
    commons = [most_common(i, input) for i in range(len(input[0]))]
    return [commons[0]] + doit([i[1:] for i in input if i[0] == commons[0]])

def doit2(input):
    if len(input) == 1:
        return input
    commons = [least_common(i, input) for i in range(len(input[0]))]
    return [commons[0]] + doit2([i[1:] for i in input if i[0] == commons[0]])


if __name__ == "__main__":
    print(int("".join(doit(input)), 2) * int("".join(doit2(input)), 2))
