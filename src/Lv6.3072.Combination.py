#-*- Coding:utf8 -*-

def Combination(n, m):
    c = 1
    for i in range(n, n - m, -1):
        c *= i
    for i in range(m, 0, -1):
        c /= i
    return int(c)

n = int(input())
m = int(input())

c = Combination(n, m)
print(c)
