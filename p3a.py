#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def most_common(index, input):
    count = sum(1 if line[index] == "1" else -1 for line in input)
    return  "1" if count > 0 else "0"

def least_common(index, input):
    count = sum(1 if line[index] == "1" else -1 for line in input)
    return  "1" if count < 0 else "0"

def doit(input):
    gamma = int(f"0b{''.join([most_common(i, input) for i in range(len(input[0]))])}", 2)
    ep = int(f"0b{''.join([least_common(i, input) for i in range(len(input[0]))])}", 2)
    return gamma * ep

if __name__ == "__main__":
    print(doit(input))
