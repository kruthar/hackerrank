import sys

message_length = int(sys.stdin.next().strip())
message = sys.stdin.next().strip()
k = int(sys.stdin.next().strip())
wheeldown = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 2
wheelup = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] * 2
wheel = wheeldown + wheelup

result = ""

while k > 26:
    k -= 26

for char in message:
    if char in wheel:
        result += wheel[wheel.index(char) + k]
    else:
        result += char
print result