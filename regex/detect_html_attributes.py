import sys
import re

import operator

numlines = int(sys.stdin.next())
tag_pattern = r'<\s*(\w+)(.*?)>'
attributes_pattern = r' (\w+)='
tags = dict()

for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.findall(tag_pattern, line)

    if m != None:
        for tag in m:
            type = tag[0]
            attribute_string = tag[1]
            if type not in tags:
                tags[type] = []
            attributes = re.findall(attributes_pattern, attribute_string)

            if attributes != None:
                for attribute in attributes:
                    if attribute not in tags[type]:
                        tags[type] += [attribute]

for result in sorted(tags.items(), key=operator.itemgetter(0)):
    print "%s:%s" % (result[0], ",".join(sorted(result[1])))


