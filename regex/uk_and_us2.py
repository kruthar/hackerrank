import sys
import re

numlines = int(sys.stdin.next())
lines = []

for i in range(0, numlines):
    lines.append(sys.stdin.next().strip())

numwords = int(sys.stdin.next())

for j in range(0, numwords):
    word1 = sys.stdin.next().strip()
    word2 = word1
    if "our" in word1:
        word2 = word2.replace("our", "or")
    elif "or" in word1:
        word2 = word2.replace("or", "our")

    word1_match = re.compile(r"\b%s\b" % word1)
    word2_match = re.compile(r"\b%s\b" % word2)
    count = 0

    for line in lines:
        m1 = word1_match.findall(line)
        m2 = word2_match.findall(line)
        count += len(m1) + len(m2)
    print count