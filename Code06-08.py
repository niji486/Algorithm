# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:33:39 2021

@author: joann
"""

## 함수

def isStackFull() : # 스택이 꽉 찼는지 확인하여 꽉찼으면 True return
    global size, stack, top 
    if (top == size-1 ) : 
        return True
    else : return False

def push(data) : 
    global size, stack, top
    if (isStackFull() == True) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

## 전역
size = 5
stack = [ None for _ in range(size)]  # = stack = [None,None,None,None,None]
top = -1

## 메인
push('커피1');push('커피2');push('커피3');push('커피4');push('커피5')
print('바닥|', stack)

push('커피6')