import sys

entries = int(sys.stdin.next().strip())

for entry in range(0, entries):
    grid_dimensions = map(int, sys.stdin.next().strip().split(" "))
    grid = []
    for a in range(0, grid_dimensions[0]):
        grid.append(map(int, list(sys.stdin.next().strip())))

    search_dimensions = map(int, sys.stdin.next().strip().split(" "))
    search = []
    for b in range(0, search_dimensions[0]):
        search.append(map(int, list(sys.stdin.next().strip())))

    finished = False
    for x in range(0, grid_dimensions[0] - search_dimensions[0] + 1):
        for y in range(0, grid_dimensions[1] - search_dimensions[1] + 1):
            if grid[x][y] == search[0][0]:
                found = True
                for i, row in enumerate(search):
                    if grid[x + i][y:y + search_dimensions[1]] != row:
                        found = False
                        break
                if found:
                    finished = True
                    print 'YES'
                    break
        if finished:
            break

    if not finished:
        print 'NO'
