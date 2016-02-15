import sys
import math

num_dots = int(sys.stdin.next().strip())
dots = []

for i in range(0, num_dots):
    dots.append(map(int, sys.stdin.next().strip().split(" ")))

max = 0
distances = dict()
for x in range(0, len(dots)):
    for y in range(x + 1, len(dots)):
        a = dots[x]
        b = dots[y]
        key = ",".join(sorted([",".join(sorted(map(str,a))), ",".join(sorted(map(str,b)))]))

        if not distances.has_key(key):
            distance = round(math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)), 6)
            if distance > max:
                max = distance
            distances[key] = distance

print max