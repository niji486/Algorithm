# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:30:53 2021

@author: joann
"""

## 함수
def add_data(friend) :  # 함수 = function = 기능
    Katok.append(None)
    Klen=len(Katok)
    Katok[Klen-1]=friend

def insert_data(position, friend) :
    Katok.append(None)
    Klen=len(Katok)
    for i in range(Klen-1, position, -1):
        Katok[i]=Katok[i-1]
        Katok[i-1]=None
    Katok[position]=friend
    
def delete_data(position) :
    Klen=len(Katok)
    Katok[position]=None
    for i in range(position+1, Klen, 1):
        Katok[i-1]=Katok[i]
        Katok[i]=None
    del(Katok[Klen-1])

## 전역변수
Katok=[] # 빈 배열(리스트)

## 메인코드
# 데이터 생성
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')

# 데이터 삽입
insert_data(3,'미나')

# 데이터 삭제
delete_data(4)


print(Katok)