import sys
import re

c = r'#include<.*?>|printf|&[a-zA-Z]'
java = r'import .*?;|public class.*?{|println'
doc = ""

for line in sys.stdin.readlines():
    doc += line.strip()

c_matches = re.findall(c, doc)
java_matches = re.findall(java, doc)

if c_matches != None and len(c_matches) > 0:
    print "C"
elif java_matches != None and len(java_matches) > 0:
    print "Java"
else:
    print "Python"
