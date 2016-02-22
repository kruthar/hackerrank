import sys

tests = int(sys.stdin.next().strip())

for i in range(0, tests):
    word = sys.stdin.next().strip()
    start = 0
    end = len(word) - 1
    index = -1

    while start <= end:
        if word[start] != word[end]:
            if word[start + 1:end + 1] == word[start + 1:end + 1][::-1]:
                index = start
                break
            elif word[start:end][::-1] == word[start:end]:
                index = end
                break
        start += 1
        end -= 1

    print index