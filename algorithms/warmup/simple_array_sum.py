import sys

count = int(sys.stdin.next().strip())
numbers = sys.stdin.next().strip().split(" ")
total = 0

for number in numbers:
    total += int(number)

print total
