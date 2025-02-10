# ***********************
# -- 내장 반복문
# ***********************
import sys
for i in range(1,11):
   for j in range(1,11):
      k = i*j
      print (k, end=' ')
   print()
''' 
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 
'''
# The print() function inner loop has end=' ' which appends a space instead of default newline.
# Hence, the numbers will appear in one row.
''' 
1. import 모듈
: 말그대로 모듈 전체를 가져옵니다
2. from 모듈 import 함수 또는 변수
: 모듈 내에서 필요한 함수나 변수만을 가져옵니다.

예를 들자면 다음과 같이 쓰일수있어요


from urllib import request
: request 를 직접참조합니다.
mine = request() 로 쓰여집니다


import urllib.request
: urllib.request 로 작성합니다.
mine = urllib.request() 로 쓰여집니다

작성하신 질문을 예로들면요


import pygame, sys
: pygame, sys 모듈을 가져옵니다


from pygame.locals import *
: pygame.locals 모듈 내에 있는 모든 변수나 함수를 가져옵니다.

여기서 * 는 특정 변수나 함수가 아닌 전체를 의미합니다.
'''