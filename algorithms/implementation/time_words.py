import sys

single_strings = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
teen_strings = ['ten','eleven','twelve','thirteen','fourteen', 'fifteen','sixteen','seventeen','eighteen','nineteen']
tens_strings = ['','ten','twenty','thirty','forty','fifty','sixty']

def get_number_string(n):
    digits = map(int, list(str(n)))
    if len(digits) == 1:
        return single_strings[digits[0]]
    elif digits[0] == 1:
        return teen_strings[digits[1]]
    else:
        return tens_strings[digits[0]] + ' ' + single_strings[digits[1]]

def round_hour(h):
    if h > 12:
        return 1
    return h

hour = int(sys.stdin.next().strip())
minute = int(sys.stdin.next().strip())

if minute == 0:
    print single_strings[hour] + " o' clock"
elif minute == 1:
    print 'one minute past ' + single_strings[hour]
elif minute == 15:
    print 'quarter past ' + single_strings[hour]
elif minute < 30:
    print get_number_string(minute) + ' minutes past ' + single_strings[hour]
elif minute == 30:
    print 'half past ' + single_strings[hour]
elif minute == 45:
    print 'quarter to ' + single_strings[round_hour(hour + 1)]
else:
    print get_number_string(60 - minute) + ' minutes to ' + single_strings[round_hour(hour + 1)]
