import sys
import re

numlines = int(sys.stdin.next())
regex = r'https?:\/\/(?:www\.|ww2\.)?((?:[a-zA-Z0-9\-]+\.)+[a-zA-Z0-9\-]+)'
domains = []

for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.findall(regex, line)

    if m != None:
        domains = set(domains) | set(m)

print ';'.join(sorted(domains))

