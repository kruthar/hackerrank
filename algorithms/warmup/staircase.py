import sys

levels = int(sys.stdin.next().strip())
count = 1

for i in range(1, levels + 1):
    print ' ' * (levels - i) + '#' * i