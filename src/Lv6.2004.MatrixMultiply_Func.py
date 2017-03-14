#-*- Coding:utf8 -*-

def mxMultiply(a, b):
    size = int(len(b))
    #height = len(a[0])
    c = []
    #init
    for i in range(size):
        c.append([])
        for j in range(size):
            c[i].append(0)
    #calc
    for i in range(size):
        for j in range(size):
            summ = 0
            for k in range(int(len(a[0]))):
                summ += a[i][k] * b[k][j]
            c[i][j] = summ
    return c

def mxInput(a):
    a_str = []
    for i in range(int(len(a))):
        a_str.append(input())
    for i in range(int(len(a))):
        a[i] = a_str[i].split()
    for i in range(int(len(a))):
        for j in range(int(len(a[i]))):
            a[i][j] = int(a[i][j])
    return a

def Print2DArr(arr):
    for i in range(int(len(arr))):
        for j in range(int(len(arr[i]))):
            print("%-5d"%int(arr[i][j]), end = '')
        else:
            print('')
    return
    
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a = mxInput(a)
b = mxInput(b)

c = mxMultiply(a, b)
Print2DArr(c)
