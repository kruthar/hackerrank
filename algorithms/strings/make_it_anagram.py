import sys

a = sorted(sys.stdin.next().strip())
b = sorted(sys.stdin.next().strip())
i = 0
deletions = 0

while i < len(a) and i < len(b):
    if a[i] == b[i]:
        i += 1
    elif a[i] < b[i]:
        del a[i]
        deletions += 1
    else:
        del b[i]
        deletions += 1

deletions += abs(len(a) - len(b))

print deletions