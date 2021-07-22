# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:33:39 2021

@author: joann
"""

## 함수
def isStackFull() : # 스택 꽉 확인
    global SIZE, stack, top
    if (top == SIZE-1) :
        return True
    else :
        return False

def push(data) : # 푸쉬
    global SIZE, stack, top
    if (isStackFull() == True) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data
    
def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False
    
def pop():
    global SIZE, stack, top
    if (isStackEmpty() == True):
        print('스택 텅!')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() : # 다음 확인만!
    global SIZE, stack, top
    if (isStackEmpty() == True):
        print('스택 텅!')
        return None
    return stack[top]
    

## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피1');push('커피2');push('커피3')
print( '바닥 |', stack)
retData = pop()
print('빼낸 것-->', retData)
retData2 = peek()
print('다음에 나올 것-->', retData2)