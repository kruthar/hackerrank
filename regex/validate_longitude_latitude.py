import sys
import re

numlines = int(sys.stdin.next())
regex = r'^\([-+]?(90(\.0+)?|[1-8]?\d(\.\d+)?), [-+]?(1(80(\.0+)?|[0-7]\d(\.\d+)?)|[1-9]\d(\.\d+)?|\d(\.\d+)?)\)$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m == None:
        print "Invalid"
    else:
        print "Valid"