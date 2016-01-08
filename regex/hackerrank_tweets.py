import sys
import re

numlines = int(sys.stdin.next())
regex = r'hackerrank'
count = 0

for i in range(0, numlines):
    line = sys.stdin.next().strip()
    lowercase_line = line.lower()
    m = re.findall(regex, lowercase_line)

    if m != None and len(m) > 0:
        count += 1

print count