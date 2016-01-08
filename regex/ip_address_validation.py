import sys
import re

numlines = int(sys.stdin.next())
ipv4 = r'^(\d{1,3})\.(\d{1,3}).(\d{1,3}).(\d{1,3})$'
ipv6 = r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    v4 = re.match(ipv4, line)
    v6 = re.match(ipv6, line)
    result = "Neither"

    if v4 != None and len(v4.groups(0)) == 4:
        v4_success = True
        for group in v4.groups(0):
            num = int(group)
            if num < 0 or num > 255:
                v4_success = False
                break
        if v4_success:
            result = "IPv4"
    elif v6 != None:
        result = "IPv6"

    print result

