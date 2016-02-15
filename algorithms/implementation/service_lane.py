import sys

params = sys.stdin.next().strip().split(" ")
num_segments = int(params[0])
num_tests = int(params[1])
segments = map(int, sys.stdin.next().strip().split(" "))

for i in range(0, num_tests):
    points = map(int, sys.stdin.next().strip().split(" "))
    vehicle = 3
    for j in range(points[0], points[1] + 1):
        if segments[j] < vehicle:
            vehicle = segments[j]
    print vehicle