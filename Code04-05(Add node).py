# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:47:03 2021

@author: joann
"""

## 함수, 클래스 
class Node(): #클래스(붕어빵틀)는 대문자로 시작하는 것이 관례
    def __init__(self):
        self.data = None
        self.link = None # 클래스로 노드구조(데이터+링크)를 만들어놓음
        
def printNodes(start) : 
    current = start
    print(current.data, end=' ')
    while current.link != None : 
        current = current.link
        print(current.data, end=' ')
    print()

# 처음에 추가하는 함수
def insert_node(findData, insertData) :
    global memory, head, current, pre  #전역범수 지시 
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head= node
        memory.append(node)
        return
    current = head 
    while current.link !=None :
        pre = current #연결유지를 위한 pre에다가 current 를 잡는 형태
        current = current.link
        if (current.data == findData) : 
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    
        
    
#중간에 추가하는 함수

    
        
## 전역

# 노드의 저장소 = 메모리,  head, pre, current 변수 숙지 
memory=[]
head, current, pre = None, None, None
# 실제 데이터 집합(실무 DB, 웹크롤링, 센서신호....)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
# 메모리상에 집어넣기
memory.append(node)

# 그외 노드(반복작업)
for data in dataArray[1: ] : #['정연', '쯔위', '사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node) 

printNodes(head)

insert_node('다현','화사')
printNodes(head)
insert_node('사나', '솔라')
printNodes(head)
insert_node('재남', '문별')
printNodes(head)