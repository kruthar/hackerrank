import sys

lines = int(sys.stdin.next().strip())

gems = dict()

for i in range(0, lines):
    elements = set(sys.stdin.next().strip())
    for element in elements:
        gems[element] = gems.get(element, 0) + 1

result = 0

for key, value in gems.iteritems():
    if value == lines:
        result += 1

print result