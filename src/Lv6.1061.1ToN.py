#-*- Coding:utf8 -*-

def Sigma(n):
    if n == 0:
        return n
    else:
        return n + Sigma(n - 1)

print(Sigma(int(input())))
        
