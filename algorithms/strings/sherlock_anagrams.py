import sys

def isAnagram(a, b):
    aS = sorted(a)
    bS = sorted(b)

    for i in range(0, len(aS)):
        if aS[i] != bS[i]:
            return False
    return True

tests = int(sys.stdin.next().strip())

for i in range(0, tests):
    word = sys.stdin.next().strip()
    anapairs = 0

    for aStart in range(0, len(word) - 1):
        for aLen in range(1, len(word) - aStart):
            for bStart in range(aStart + 1, len(word) - aLen + 1):
                if isAnagram(word[aStart:aStart + aLen], word[bStart:bStart + aLen]):
                    anapairs += 1
    print anapairs
