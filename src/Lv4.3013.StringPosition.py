#-*- Coding:utf8 -*-

def strcp(source, mask):
    lst = []
    for i in range(int(len(source))):
        for j in range(int(len(mask))):
            if source[(i + j)] != mask[j]:
                break
        else:
            lst.append(i)
    return lst

str1 = input()
str2 = input()

lst = strcp(str1, str2)
for i in range(int(len(lst))):
    print(lst[i])
