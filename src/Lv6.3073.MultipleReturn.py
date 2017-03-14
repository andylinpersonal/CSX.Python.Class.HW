#-*- Coding:utf8 -*-

def TestFunc(n = 0):
    sum = 0; product = 1;
    for i in range(1, n + 1):
        sum += i
        product *= i
    return sum, product

s, p = TestFunc(int(input()))
print('%d\n%d'%(p, s))
