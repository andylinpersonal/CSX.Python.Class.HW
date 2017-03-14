#-*- coding:utf8 -*-

answer = input()
ifPass = False
while not ifPass:
    acnt = 0
    bcnt = 0
    numlst = []
    guess = input()
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            acnt += 1
    for i in range(len(guess)):
        if guess[i] not in numlst:
            for j in range(len(answer)):
                if (j != i) and (answer[j] == guess[i]):
                    bcnt += 1
            numlst.append(guess[i])
    print('%dA%dB'%(acnt, bcnt))
    if (acnt == 4) and (bcnt == 0):
        print('You Win!')
        break
