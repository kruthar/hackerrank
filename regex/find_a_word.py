import sys
import re

numlines = int(sys.stdin.next())
lines = []

for i in range(0, numlines):
    lines.append(sys.stdin.next().strip())

numwords = int(sys.stdin.next())

for j in range(0, numwords):
    word = sys.stdin.next().strip()
    regex = re.compile(r"\b%s\b" % word)
    count = 0

    for line in lines:
        m = regex.findall(line)
        count += len(m)
    print count