# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:22:42 2021

@author: joann
"""

## 함수 
def add_data(friend) :  # 함수 = function = 기능
    katok.append(None)
    Klen=len(katok)
    katok[Klen-1]=friend

def insert_data(position, friend) :
    katok.append(None)
    Klen=len(katok)
    for i in range(Klen-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position]=friend
    
def delete_data(position) :
    Klen=len(katok)
    katok[position]=None
    for i in range(position+1, Klen, 1):
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[Klen-1])


## 전역
katok = []
select = -1 #1추가, 2삽입, 3삭제, 4종료, 옵션의 초기값은 관례적으로 아무도 안할 것 같은 -1


## 메인
while (select !=4) :
    select = int(input('선택(1추가, 2삽입, 3삭제, 4종료)-->'))
                 
    if (select == 1) :
        data = input('추가할 친구-->') # 추가작동
        add_data(data)
        print(katok)
    elif(select == 2) :
        pos = int(input('삽입 위치-->'))
        data = input('삽입할 데이터 -->')
        insert_data(pos,data)
        print(katok)# 삽입작동
    elif(select == 3) : 
        pass # 삭제작동
    elif(select == 4) :
        pass # 종료
    else : 
        print('잘못 입력!')
        
