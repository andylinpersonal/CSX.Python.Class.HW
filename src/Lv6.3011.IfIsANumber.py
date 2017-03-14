#-*- Coding:utf8 -*-

inp = input()

IsNumber = True
for i in range(len(inp)):
    if not '0' <= inp[i] <= '9':
        IsNumber = False
        break
else:
    print('n=%d'%(int(inp)))
if not IsNumber:
    print('is not a number')
