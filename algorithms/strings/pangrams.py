import sys

sentence = sys.stdin.next().strip().lower()
satisfied = True

for ord in range(ord('a'), ord('z') + 1):
    if chr(ord) not in sentence:
        satisfied = False
        break

if satisfied:
    print 'pangram'
else:
    print 'not pangram'