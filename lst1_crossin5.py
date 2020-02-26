# -*- coding: utf-8 -*-
#P1
a=0
for i in range(3,100,3):
   a=a+i
print(a)

#P2
height=int(input('请输入高度'))
width=int(input('请输入宽度'))
for i in range(1,height+1):
  print('*'*width)

#P3
for i in range(1, 10):
  for j in range(1,10):
      print('%d x %d = %d' %(i,j,i*j))

#P4
nums = [23, 45, 8, 13, 50, 43, 21]
sum = 0
for n in nums:
  sum=sum+n
  if sum > 100:
      break
print(sum)
