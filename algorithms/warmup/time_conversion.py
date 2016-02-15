import sys
import re

time = sys.stdin.next().strip()
regex = r'^(\d\d):(\d\d):(\d\d)(AM|PM)'

m = re.match(regex, time)

if m.group(4) == "AM":
    if m.group(1) == '12':
        print "00:%s:%s" % (m.group(2), m.group(3))
    else:
        print "%s:%s:%s" % (m.group(1), m.group(2), m.group(3))
else:
    if m.group(1) == '12':
        print "%s:%s:%s" % (m.group(1), m.group(2), m.group(3))
    else:
        print "%d:%s:%s" % (int(m.group(1)) + 12, m.group(2), m.group(3))