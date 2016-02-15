import sys

num_lines = int(sys.stdin.next().strip())

for i in range(0, num_lines):
    num_string = sys.stdin.next().strip()
    num = int(num_string)
    divs = 0

    for digit in num_string:
        if digit != '0' and num % int(digit) == 0:
            divs += 1

    print divs