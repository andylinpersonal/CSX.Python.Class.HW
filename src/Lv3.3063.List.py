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
cnt = 0
for i in range(len(numlst)):
    if numlst[i] == 10:
        cnt += 1
print(cnt)

numlst.append(10)
numlst.sort()
print(numlst)

numlst.reverse()
print(numlst)
