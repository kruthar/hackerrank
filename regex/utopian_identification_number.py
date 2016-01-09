import sys
import re

numlines = int(sys.stdin.next())
regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m == None:
        print "INVALID"
    else:
        print "VALID"

