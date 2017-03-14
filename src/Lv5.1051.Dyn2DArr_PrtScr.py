#-*- Coding:UTF8 -*-

def TableAlloc(Row, Column):
    out = []
    for i in range(Row):
        out.append([])
        for j in range(Column):
            out[i].append(0)
    return out
def TableAssign(lst):
    for i in range(int(len(lst))):
        tmpLst = input().split()
        for j in range(int(len(lst[i]))):
            lst[i][j] = eval(tmpLst[j])
    return lst

m = int(input())
n = int(input())

sc = TableAlloc(m, n)
sc = TableAssign(sc)

total = 0; itemcnt = 0
for i in range(int(len(sc))):
    print('class %d'%(i + 1))
    summ = 0
    for j in range(int(len(sc[i]))):
        itemcnt += 1
        summ += sc[i][j]
        print(' %d: %d'%((j + 1), sc[i][j]))
    total += summ
    print(' sum: %d\n avg: %.2f'%(summ, summ / int(len(sc[i]))))
print('total: %d, avg: %.2f'%(total, total / itemcnt))
