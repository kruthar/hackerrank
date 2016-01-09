import sys
import re

doc = ""
regex = r'question-summary-(.*?)".*?<div class="summary">.*?<.*?h3.*?<.*?a.*?>(.*?)<.*?asked.*?<span.*?>(.*?)<'


for line in sys.stdin.readlines():
    doc += line.strip()

m = re.findall(regex, doc)

if m != None:
    for match in m:
        print ';'.join(match)

