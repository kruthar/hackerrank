import sys
import re

numlines = int(sys.stdin.next())
lines = []

for i in range(0, numlines):
    lines.append(sys.stdin.next().strip())

numwords = int(sys.stdin.next())

for j in range(0, numwords):
    word1 = sys.stdin.next().strip()
    word2 = ""
    if word1.endswith('ze'):
        word2 = word1[:-2] + 'se'
    elif word1.endswith('se'):
        word2 = word1[:-2] + 'ze'

    word1_match = re.compile(r"\b%s\b" % word1)
    word2_match = re.compile(r"\b%s\b" % word2)
    count = 0

    for line in lines:
        m1 = word1_match.findall(line)
        m2 = word2_match.findall(line)
        count += len(m1) + len(m2)
    print count