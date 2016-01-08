import sys
import re

numlines = int(sys.stdin.next())
regex = r'^[_\.]\d+[a-zA-Z]*_?$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m == None:
        print "INVALID"
    else:
        print "VALID"

