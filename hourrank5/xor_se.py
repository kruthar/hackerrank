import sys

def xor(a, b):
    bin_a = str(bin(a)).split('b')[1]
    bin_b = str(bin(b)).split('b')[1]

    while len(bin_a) < len(bin_b):
        bin_a = '0' + bin_a

    while len(bin_b) < len(bin_a):
        bin_b = '0' + bin_b

    result = ''
    for i in range(0, len(bin_a)):
        if bin_a[i] != bin_b[i]:
            result += '1'
        else:
            result += '0'

    return int(result, 2)

def get_array(n):
    result = [0]

    for i in range(1, n):
        result.append(xor(result[-1], i))

    return result


q = int(sys.stdin.next().strip())

for i in range(0, q):
    l, r = map(int, sys.stdin.next().strip().split(" "))
    sub_arr = get_array(r + 1)[l:]
    result = sub_arr[0]

    for j in sub_arr[1:]:
        result = xor(result, j)

    print result