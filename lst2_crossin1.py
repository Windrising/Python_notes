# -*- coding: utf-8 -*-
import random

a=random.randint(1,100)
n=1
print('请输入0~100的一个数字')
while True:
   b=int(input())
   if b==a:
      print('恭喜你答对了！您一共答了%d轮'%n)
      break
   if b<a:
      n+=1
      print('您输入的数字偏小，请继续猜')
   if b>a:
      n+=1
      print('您输入的数字偏大，请继续猜')
