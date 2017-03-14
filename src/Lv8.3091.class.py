#!/usr/bin/env python3
#-*- coding:utf8 -*-
import os
class student:
    '''
    說明文件區塊必須緊鄰class宣告
    This is readme of class student
    '''
    name = ''
    gender = ''
    grades = []

    def __init__(self):
        self.name = input()
        self.gender = input()

    def avg(self):
        summ = 0
        for i in range(len(self.grades)):
            summ += self.grades[i]
        return summ / int(len(self.grades))

    def add(self, grade):
        self.grades.append(int(grade))

    def fcount(self):
        cnt = 0
        for i in range(len(self.grades)):
            if self.grades[i] < 60:
                cnt += 1

person = student()

for i in range(3):
    person.add(input())
print(student.name)
print(student.avg())
print(student.fcount())