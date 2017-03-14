#-*- Coding:UTF8 -*-

n = int(input())
lst = []
str1 = ''
for i in range(1, n+1):
    lst.append("data " + str(i))
for i in range(n):
    str1 = lst.pop()
    print(str1)
    lst.insert(0, str1)
print('')
for i in range(n):
    print(lst[i])
