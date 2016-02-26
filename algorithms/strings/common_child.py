import sys

def common_child(a, b, level):
    #print ' '*level, a, b

    if len(a) == 0 or len(b) == 0:
        return 0

    result = max(common_child(a[1:], b, level + 1), common_child(a, b[1:], level + 1))

    if b[0] in a:
        result = max(common_child(a[a.index(b[0]) + 1:], b[1:],level + 1) + 1, result)

    if a[0] in b:
        result = max(common_child(a[1:], b[b.index(a[0]) + 1:],level + 1) + 1, result)

    return result

a = sys.stdin.next().strip()
b = sys.stdin.next().strip()

# WEWOUCUIDGCGTRMEZEXZFEJWIRBBYXAYDFEJJDLEBVHHK
# WE   C      HMRXZWMLRYUCOCZHJRRJBOAJOJZZVUYXIC
# FDAGCXGKCTKWECHMRXZWMLRYUCOCZHJRRJBOAJOJZZVUYXIC

aset = set(a)
bset = set(b)

intersection = aset.intersection(bset)

ashort = ''
bshort = ''

for i in a:
    if i in intersection:
        ashort += i

for j in b:
    if j in intersection:
        bshort += j

print common_child(a, b, 0)