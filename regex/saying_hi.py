import sys
import re

numlines = int(sys.stdin.next())
regex = r'^[Hh][Ii] [^dD].*$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m != None:
        print line

