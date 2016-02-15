import sys

def flattenRing(grid, left, right, top, bottom):
    stripe = []

    stripe += grid[top][left:right + 1]
    for a in range(top + 1, bottom + 1):
        stripe.append(grid[a][right])
    stripe += reversed(grid[bottom][left:right])
    for b in reversed(range(top + 1, bottom)):
        stripe.append(grid[b][left])
    return stripe

def rotateString(string, n):
    n = n % len(string)
    return string[n:] + string[0:n]

def reassembleGrid(dimensions, stripes):
    grid = []

    for r in range(0, dimensions[0]):
        grid.append([0] * dimensions[1])

    for i, stripe in enumerate(stripes):
        left = i
        right = dimensions[1] - 1 - i
        top = i
        bottom = dimensions[0] - 1 - i
        count = 0

        for w in range(left, right + 1):
            grid[top][w] = stripe[count]
            count += 1
        for x in range(top + 1, bottom + 1):
            grid[x][right] = stripe[count]
            count += 1
        for y in reversed(range(left, right)):
            grid[bottom][y] = stripe[count]
            count += 1
        for z in reversed(range(top + 1, bottom)):
            grid[z][left] = stripe[count]
            count += 1

    return grid

input = map(int, sys.stdin.next().strip().split(" "))
dimensions = input[0:2]
rotations = input[2]

grid = []

for i in range(0, dimensions[0]):
    grid.append(map(int, sys.stdin.next().strip().split(" ")))

left = 0
right = dimensions[1] - 1
top = 0
bottom = dimensions[0] - 1

stripes = []

while left <= right and top <= bottom:
    stripes.append(flattenRing(grid, left, right, top, bottom))
    left += 1
    right -= 1
    top += 1
    bottom -= 1

for s in range(0, len(stripes)):
    stripes[s] = rotateString(stripes[s], rotations)

for row in reassembleGrid(dimensions, stripes):
    print ' '.join(map(str, row))

