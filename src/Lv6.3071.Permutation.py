#-*- Coding:utf8 -*-

def Permutation(n, m):
    p = 1
    for i in range(n, n - m, -1):
        p *= i
    return p

n = int(input())
m = int(input())

p = Permutation(n, m)
print(p)
