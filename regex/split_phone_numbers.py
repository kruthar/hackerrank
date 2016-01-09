import sys
import re

numlines = int(sys.stdin.next())
regex = r'^(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m != None and m.groups(0) != None:
        print "CountryCode=%s,LocalAreaCode=%s,Number=%s" % (m.group(1), m.group(2), m.group(3))
