# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:22:00 2021

@author: joann
"""

## 함수



## 변수
stack = [None, None, None, None, None]
top = -1    # -1 --> 초기값, top은 위치네비게이터같은 성격



## 메인
top += 1
stack[top]='커피'
top += 1
stack[top]='녹차'
print('바닥 |', stack)

# Pop 구현
data = stack[top]
stack[top]= None
top -= 1
print('추출 --> ', data)
print('바닥 |', stack)

data = stack[top]
stack[top]= None
top -= 1
print('추출 --> ', data)
print('바닥 |', stack)