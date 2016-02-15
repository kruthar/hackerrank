import sys

n = int(sys.stdin.next().strip())
max = 0

for a in range(1, n - 2):
    for b in range(a, n - 1):
        volume = a * b * (n - a - b)
        if volume > max:
            max = volume

print max