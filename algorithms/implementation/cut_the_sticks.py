import sys

num_sticks = int(sys.stdin.next().strip())
sticks = map(int, sys.stdin.next().strip().split(" "))

while len(sticks) > 0:
    print len(sticks)
    sticks[:] = [stick - min(sticks) for stick in sticks]
    while 0 in sticks:
        sticks.remove(0)