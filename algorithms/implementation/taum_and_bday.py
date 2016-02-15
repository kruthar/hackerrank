import sys

cases = int(sys.stdin.next().strip())

for case in range(0, cases):
    b, w = map(int, sys.stdin.next().strip().split(" "))
    x, y, z = map(int, sys.stdin.next().strip().split(" "))

    bprice = x
    wprice = y

    if y + z < x:
        bprice = y + z

    if x + z < y:
        wprice = x + z

    print bprice * b + wprice * w