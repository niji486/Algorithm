# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:18:30 2021

@author: joann
"""

## 함수, 클래스 
class Node(): #클래스(붕어빵틀)는 대문자로 시작하는 것이 관례
    def __init__(self):
        self.data = None
        self.link = None # 클래스로 노드구조(데이터+링크)를 만들어놓음

## 전역


## 메인 
node1=Node()
node1.data='다현'

node2=Node()
node2.data='정연'
node1.link = node2 # node2 data 가 생성된 후 링크 생성 

node3=Node()
node3.data='쯔위'
node2.link = node3

node4=Node()
node4.data='사나'
node3.link = node4

node5=Node()
node5.data='지효'
node4.link = node5

# 새로운 멤버가 중간에 들어갈 때 '정연' -> '재남' -> '쯔위'
# newNode=Node()
# newNode.data='재남'
# newNode.link=node2.link
# node2.link=newNode


#노드 삭제 1. 링크 연결 수정 2. 노드 삭제del
node2.link=node3.link
del(node3)


# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

# 1. '다현'에서 작업시작  2. link가 없을때까지(while) 반복지시 

current = node1
print(current.data, end=' ')
while current.link != None : 
    current = current.link
    print(current.data, end=' ')
    
    




    