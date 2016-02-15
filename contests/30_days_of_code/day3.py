import sys

input = int(sys.stdin.next())

if input % 2 != 0:
    print "Weird"
else:
    if input >= 2 and input <= 5:
        print "Not Weird"
    elif input >= 6 and input <= 20:
        print "Weird"
    else:
        print "Not Weird"