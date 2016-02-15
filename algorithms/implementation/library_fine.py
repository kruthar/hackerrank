import sys
import datetime

actual = map(int, sys.stdin.next().strip().split(" "))
expected = map(int, sys.stdin.next().strip().split(" "))

actual_date = datetime.date(actual[2], actual[1], actual[0])
expected_date = datetime.date(expected[2], expected[1], expected[0])

diff = actual_date.toordinal() - expected_date.toordinal()

if diff <= 0:
    print 0
elif actual_date.year == expected_date.year:
    if actual_date.month == expected_date.month:
        print 15 * diff
    else:
        print 500 * (actual_date.month - expected_date.month)
else:
    print 10000