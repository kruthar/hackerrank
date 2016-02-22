import sys

tests = int(sys.stdin.next().strip())

for i in range(0, tests):
    a = set(sys.stdin.next().strip())
    b = set(sys.stdin.next().strip())

    if len(a.intersection(b)) > 0:
        print 'YES'
    else:
        print 'NO'