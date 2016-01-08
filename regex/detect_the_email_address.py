import sys
import re

numlines = int(sys.stdin.next())
regex = r'\b[^@\s]+@[^\s]+\.[^\s]+\b'
emails = []

for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.findall(regex, line)

    if m != None:
        emails = set(emails) | set(m)

print ';'.join(sorted(emails))

