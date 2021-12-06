#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
]

## SQ only
def transpose(array):
    out = [[] for _ in array]

    for i in range(len(array)):
        for j in range(len(array)):
            out[j].append(array[i][j])
    return out


# Returns data in a tuple:
#  (List(Int), List(List(List(Int)))
def clean_input(input):
    nums = list(map(int, input[0].split(",")))
    boards = []
    temp = []
    for line in input[2:]:
        if line == "":
            boards.append(temp)
            temp = []
        else:
            temp.append(list(map(int, filter(lambda x: x is not "", line.split(" ")))))
    boards.append(temp)

    return (nums, boards)


def doit(nums, boards):
    with_trans = boards
    for i in range(len(boards)):
        with_trans[i] += transpose(boards[i])

    for num in nums:
        for i in range(len(with_trans)):
            for line in with_trans[i]:
                try:
                    line.remove(num)
                except ValueError as _:
                    pass
                if len(line) == 0:
                    return sum(map(sum, with_trans[i][:5])) * num


if __name__ == "__main__":
    print(doit(*clean_input(input)))
