# -*- coding: utf-8 _*-
# Filename : basic.py

# 猜数字小游戏

from random import randint
num = randint (1,200)

print ('Guess what I think.')
bingo = False

while bingo == False:
    answer = int(input())

    if answer < num:
        print ('%d too small' % answer)
    if answer > num:
        print ('%d too big' % answer)
    if answer == num:
        print ('Bingo!\n%d is right.' % answer)
    bingo == True