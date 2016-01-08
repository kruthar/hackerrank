import sys
import re

single = r'^.*?(\/\/.*)$'
multi_start = r'^.*?(\/\*.*)$'
multi_end = r'^(.*?\*\/).*$'
in_multi = False

for line in sys.stdin.readlines():
    single_match = re.match(single, line.strip())
    multi_start_match = re.match(multi_start, line.strip())
    multi_end_match = re.match(multi_end, line.strip())

    if in_multi:
        if multi_end_match != None and multi_end_match.groups(0) != None:
            print multi_end_match.groups(0)[0]
            in_multi = False
        else:
            print line.strip()
    elif multi_start_match != None and multi_start_match.groups(0) != None:
        print multi_start_match.groups(0)[0]
        if multi_end_match == None or multi_end_match.groups(0) == None:
            in_multi = True
    elif single_match != None and single_match.groups(0) != None:
        print single_match.groups(0)[0]

