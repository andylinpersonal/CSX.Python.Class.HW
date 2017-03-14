#-*- Coding:UTF8 -*-

numlst = []
num = 0
while True:
    num = int(input())
    if num != -1:
        numlst.append(num)
    else:
        break
numlst.sort()
print(numlst)

numlst.insert(3, 10)
print(numlst)
numlst.sort()

cnt = 0
for i in range(len(numlst)):
    if numlst[i] == 10:
        cnt += 1
print(cnt)
numlst.reverse()
print(numlst)
