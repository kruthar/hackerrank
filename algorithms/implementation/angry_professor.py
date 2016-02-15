import sys

num_tests = int(sys.stdin.next().strip())

for i in range(1, num_tests + 1):
    params = sys.stdin.next().strip().split(" ")
    students = sys.stdin.next().strip().split(" ")
    n = int(params[0])
    k = int(params[1])
    ontime = 0

    for student in students:
        if int(student) <= 0:
            ontime += 1

    if ontime >= k:
        print "NO"
    else:
        print "YES"