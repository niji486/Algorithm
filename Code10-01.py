# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:42:16 2021

@author: joann
"""

## 함수
def countDown(n):
    if n ==0:
        print('발사!')
    else :
        print(n)
        countDown(n-1)

def printStar(n) :
    if n > 0 :
        printStar(n-1)
        print('★'* n)
        
def gugu(dan, num) :
    print("%d X %d = %d" %(dan, num, dan*num))
    if num < 9 :
        gugu(dan,num+1)

    
        
        
        
## 전역

## 메인

countDown(5)
printStar(5)

for dan in range(2,10) :
    print("## %d단 ##" % dan)
    gugu(dan,1)   