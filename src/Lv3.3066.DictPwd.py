#-*- coding:utf8 -*-

passbook = {'1':" Wor", 2.2:"gic", "Three":"rd", 4:" Ma", "Six":"ld.", 5:"A"}

codedstr = '''5-4-2.2-'1'-"Six"'''
codedlst = codedstr.split('-')
decoded = ''
for i in range(int(len(codedlst))):
    codedlst[i] = eval(codedlst[i])
for i in range(int(len(codedlst))):
    decoded += passbook[codedlst[i]]
print(decoded)
