import sys
import re

numlines = int(sys.stdin.next())
regex = r'<\s*(\w+)\s*|(\[.*?\]\(.*?\))'
tags = []

for i in range(0, numlines):
    line = sys.stdin.next()
    m = re.findall(regex, line)

    for find in m:
        for group in find:
            tag = ''
            if group.startswith("["):
                tag = 'a'
            else:
                tag = group.strip()

            if tag != '' and tag not in tags:
                tags.append(tag)
print ';'.join(sorted(tags))

