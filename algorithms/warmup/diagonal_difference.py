import sys

num_lines = int(sys.stdin.next().strip())
left = 0
right = num_lines - 1
difference = 0

for i in range(0, num_lines):
    line = sys.stdin.next().strip()
    numbers = line.split(" ")
    difference += int(numbers[left]) - int(numbers[right])
    left += 1
    right -= 1

print abs(difference)