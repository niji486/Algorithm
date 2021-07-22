# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:37:15 2021

@author: joann
"""

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear >= SIZE-1) :
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else:
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

## 메인
enQueue('화사');enQueue('솔라')
print('출구<---', queue, '<--입구')
retData = peek()
print('다음 손님 대기하세요-->',retData)

retData = deQueue()
print('입장 손님-->',retData)
retData = deQueue()
print('입장 손님-->',retData)
retData = deQueue()
print('입장 손님-->',retData)
print('출구<---', queue, '<--입구')