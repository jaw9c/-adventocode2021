#!/usr/bin/python3
from utils import load_input_as_ints
from p1a import doit

input = load_input_as_ints()

test_input = [199,200,208,210,200,207,240,269,260,263]

rolling_input = [sum(input[i:i+3]) for i in range(0, len(input) -2)]

if __name__ == "__main__":
    print(doit(rolling_input))
