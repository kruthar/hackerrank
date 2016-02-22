import sys

tests = int(sys.stdin.next().strip())

for j in range(0, tests):
    word = sys.stdin.next().strip()
    a = sorted(list(word[:len(word)/2]))
    b = sorted(list(word[len(word)/2:]))

    if len(a) != len(b):
        print -1
        continue

    i = 0
    changes = 0

    while i < len(a) and i < len(b):
        if a[i] == b[i]:
            i += 1
        elif a[i] < b[i]:
            if b[i] in a:
                a.remove(b[i])
                del b[i]
            else:
                del a[i]
                del b[i]
                changes += 1
        else:
            del b[i]

    changes += abs(len(a) - len(b))

    print changes