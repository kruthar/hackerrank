import sys
import re

numlines = int(sys.stdin.next())
regex = r'^[A-Z]{5}\d{4}[A-Z]$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m == None:
        print "NO"
    else:
        print "YES"

