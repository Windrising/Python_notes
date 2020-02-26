# -*- coding: utf-8 -*-
import random

while True:
   a=random.randint(1,100)
   times=1
   print('请输入0~100的一个数字')
   while True:
      b=int(input())
      if b==a:
         print('恭喜你答对了！您一共答了%d轮'%times)
         answer=input('请问您还要继续游戏吗？输入Y继续/其他退出')
         break
      if b<a:
         times+=1
         print('您输入的数字偏小，请继续猜')
      if b>a:
         times+=1
         print('您输入的数字偏大，请继续猜')
   if answer!='Y':
      break
