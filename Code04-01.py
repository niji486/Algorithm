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

print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')