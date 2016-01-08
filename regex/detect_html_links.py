import sys
import re

numlines = int(sys.stdin.next())
regex = r'<a.*?href="(.*?)".*?>(?:<.*?>)*(.*?)(?:<\/.*?>)*<\/a>'


for i in range(0, numlines):
    line = sys.stdin.next()
    m = re.findall(regex, line)

    for find in m:
        if len(find) == 2:
            print '%s,%s' % (find[0].strip(), find[1].strip())

