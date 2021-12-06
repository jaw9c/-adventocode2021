#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def clean_input(input):
    return [
        (list(map(int, x[0].split(","))), list(map(int, x[1].split(","))))
        for x in [x.split(" -> ") for x in input]
    ]


def doit(input):
    filtered_input = [(a, b) for (a, b) in input if a[0] == b[0] or a[1] == b[1]]

    coords = {}

    for (a, b) in filtered_input:
        (x1, y1), (x2, y2) = a, b
        if x1 <= x2:
            pointsX = range(x1, x2 + 1)
        else:
            pointsX = range(x2, x1 + 1)

        if y1 <= y2:
            pointsY = range(y1, y2 + 1)
        else:
            pointsY = range(y2, y1 + 1)

        for i in pointsX:
            for j in pointsY:
                if coords.get(str((i, j))):
                    coords[str((i, j))] = coords[str((i, j))] + 1
                else:
                    coords[str((i, j))] = 1

    return len([1 for v in coords.values() if v > 1])


if __name__ == "__main__":
    print(doit(clean_input(input)))
