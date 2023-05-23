import re

for i in range(0, 18):
    if i > 0:
        print(i, oct(i).replace("0o", "", 1), hex(i)[2:], bin(i)[2:])


def print_formatted(number):
    space = number.bit_length()
    for i in range(1, number + 1):
        print(str(i).rjust(space), oct(i)[2:].rjust(space), hex(i)[2:].upper().rjust(space), bin(i)[2:].rjust(space))


def count_substring(string, sub_string):
    match = re.findall('(?=' + sub_string + ')', string)
    return len(match)
