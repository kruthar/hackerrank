import sys

def pad(decimal):
    decimals = len(str(decimal).split('.', 2)[1])

    return str(decimal) + '0' * (6 - decimals)

count = float(sys.stdin.next().strip())
numbers = sys.stdin.next().strip()

positive = 0
negative = 0
zero = 0

for number in numbers.split(" "):
    if int(number) > 0:
        positive += 1
    elif int(number) < 0:
        negative += 1
    else:
        zero += 1

print pad(round(positive / count, 6))
print pad(round(negative / count, 6))
print pad(round(zero / count, 6))

