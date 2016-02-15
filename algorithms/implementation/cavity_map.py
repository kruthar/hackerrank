import sys

size = int(sys.stdin.next().strip())

grid = []
result = []

for i in range(0, size):
    line = map(int,list(sys.stdin.next().strip()))
    grid.append(line)
    result.append(line)

for row in range(1, size - 1):
    for col in range(1, size - 1):
        cur = grid[row][col]
        if cur > grid[row - 1][col] and cur > grid[row + 1][col] and cur > grid[row][col - 1] and cur > grid[row][col + 1]:
            result[row][col] = 'X';

for x in result:
    print ''.join(map(str,x))