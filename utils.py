#!/usr/bin/python3
import sys

def load_input_as_ints():
    with open(sys.argv[1]) as f:
        return list(map(int, f.read().split("\n")))
