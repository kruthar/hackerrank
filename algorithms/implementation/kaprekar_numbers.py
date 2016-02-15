import sys

min = int(sys.stdin.next().strip())
max = int(sys.stdin.next().strip())

results = []

for i in range(min, max + 1):
    square = str(i * i)
    left = square[0:len(square)/2]
    right = square[len(square)/2:]

    if left == '':
        left = '0';
    if right == '':
        right = '0';

    if int(left) + int(right) == i:
        results.append(str(i))

if len(results) > 0:
    print ' '.join(results)
else:
    print 'INVALID RANGE'