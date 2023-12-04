#!/usrbin/env python

from curses.ascii import isdigit

digits = dict(
    one=1,
    two=2,
    three=3,
    four=4,
    five=5,
    six=6,
    seven=7,
    eight=8,
    nine=9,
)

def get_first_digit(input_str: str) -> int:
    for index, item in enumerate(input_str):
        if item.isdigit():
            return int(item)
        
        for key, value in digits.items():
            if input_str[index:].startswith(key):
                return value
            

def get_last_digit(input_str: str) -> int:
    start = len(input_str) - 1

    while start >= 0:
        if input_str[start:start+1].isdigit():
            return int(input_str[start:start+1])
        
        for key, value in digits.items():
            local_start = start - len(key) + 1
            if input_str[local_start:].startswith(key):
                return value
        start -= 1

def validate(input_line: str) -> int:
    first_digit = get_first_digit(input_line)
    last_digit = get_last_digit(input_line)
    return int(f"{first_digit}{last_digit}")

if "__main__" ==  __name__:
    with open("./input.txt", "r")  as data:
        lines = data.readlines()

    running_total = 0

    for line in lines:
        running_total += validate(line)
    print(running_total)
