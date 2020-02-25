# -*- coding: utf-8 -*-
#P1
a=30
print('请输入0~100的一个数字')
while True:
   b=int(input())
   if b==a:
      print('恭喜你答对了！')
      break
   if b<a:
      print('您输入的数字偏小，请继续猜')
   if b>a:
      print('您输入的数字偏大，请继续猜')

#P2
count=0
while count<10:
   count += 1
   str_count=str(count)
   if '4' in str_count or '5'in str_count:
      continue
   print(count)

#P3
count=[]
a=0
while a<99:
   a+=3
   count=count+[a]
print(sum(count))
