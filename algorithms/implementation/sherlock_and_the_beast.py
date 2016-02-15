import sys

num_lines = int(sys.stdin.next().strip())

for i in range(0, num_lines):
    n = int(sys.stdin.next().strip())

    found = False

    remainder5s = n % 3
    while remainder5s <= n:
        if remainder5s % 5 == 0:
            print '5' * (n - remainder5s) + '3' * remainder5s
            found = True
            break
        remainder5s += 3

    if found:
        continue

    if n % 5 == 0:
        print '3' * n
        continue

    print -1

