import sys
import math

message = sys.stdin.next().strip()

lower = int(math.floor(math.sqrt(len(message))))
upper = int(math.ceil(math.sqrt(len(message))))

min_bounds = (lower, upper)
min_area = lower * upper

for l in range(lower, upper + 1):
    for u in range(l, upper + 1):
        if l * u >= len(message) and l * u < min_area:
            min_bounds = (l, u)
            min_area = l * u

grid = []

for row in range(0, min_bounds[0] + 1):
    grid.append(message[row * min_bounds[1]:row * min_bounds[1] + min_bounds[1]])

secret = []
for col in range(0, min_bounds[1]):
    word = ''
    for row in range(0, min_bounds[0] + 1):
        if col < len(grid[row]):
            word += grid[row][col]
    secret.append(word)

print ' '.join(secret)