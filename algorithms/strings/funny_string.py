import sys

tests = int(sys.stdin.next().strip())

for test in range(0, tests):
    word = sys.stdin.next().strip()
    rev = word[::-1]
    satisfied = True

    for i in range(1, len(word)):
        if abs(ord(word[i]) - ord(word[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            satisfied = False
            break

    if satisfied:
        print 'Funny'
    else:
        print 'Not Funny'