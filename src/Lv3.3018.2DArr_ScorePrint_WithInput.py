#-*- Coding:utf8 -*-
#parser
lst = []
for i in range(5):
    inStr = input()
    inStr += ' '
    cnt = 0; numlst = []; digiLst = []
    for j in range(len(inStr)):
        if ('0' <= inStr[j] <= '9'):
            digiLst.append(int(inStr[j]))
        elif len(digiLst) != 0:
            sum = 0
            for k in range(len(digiLst)):
                sum += digiLst[k] * 10 ** (len(digiLst) - k - 1)
            numlst.append(sum)
            print(digiLst)
            digiLst = []
    lst.append(numlst)
print(lst)
#output
total = 0; highestID = 0; highestAvg = 0
for i in range(0, len(lst)):
    print('student %d'%(i + 1))
    sum = 0; avg = 0
    for j in range(0, len(lst[i])):
        print(' %d: %d'%(j + 1, lst[i][j]))
        sum += lst[i][j]
        total += lst[i][j]
    print(' sum: %d\n avg: %.2f'%(sum, sum/len(lst[i])))
    if sum/len(lst[i]) > highestAvg:
        highestAvg = sum/len(lst[i])
        highestID = i
print('total: %d, avg: %.2f'%(total, total/(len(lst) * len(lst[0]))))
print('highest avg: student %d: %.2f'%(highestID + 1, highestAvg))
