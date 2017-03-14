#-*- Coding:utf8 -*-

lst = [[76, 73, 85],
       [88, 84, 76],
       [92, 82, 92],
       [82, 91, 85],
       [72, 74, 73]]
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
