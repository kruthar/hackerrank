import sys

numlines = int(sys.stdin.next())
term = "hackerrank"

for i in range(0, numlines):
    line = sys.stdin.next()
    words = line.strip().split(" ")

    if len(words) == 0:
        print -1
    else:
        front = words[0][0:len(term)] == term
        back = words[-1][-len(term):] == term

        if front and back:
            print 0
        elif front:
            print 1
        elif back:
            print 2
        else:
            print -1