#-*- Coding:utf8 -*-

IsNotNumber = True
while IsNotNumber:
    inp = input()

    IsNotNumber = False
    for i in range(len(inp)):
        if not '0' <= inp[i] <= '9':
            IsNotNumber = True
            break
    else:
        print('n=%d'%(int(inp)))
    if IsNotNumber:
        print('is not a number')
