#!/usrbin/env python

from curses.ascii import isdigit


def get_first_digit(input_str: str) -> int:
    for char in input_str:
        if char.isdigit():
            return char

def validate(input_line: str) -> int:
    first_digit = get_first_digit(input_line)
    last_digit = get_first_digit(input_line[::-1])
    return int(f"{first_digit}{last_digit}")

if "__main__" ==  __name__:
    with open("./input.txt", "r")  as data:
        lines = data.readlines()

    running_total = 0

    for line in lines:
        running_total += validate(line)
    print(running_total)
