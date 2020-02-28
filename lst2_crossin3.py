# -*- coding: utf-8 -*-
import random

#Guess
name=input('请输入玩家姓名：')
n=0  #总游戏数
cycle=[]

while True:
   number=random.randint(1,100)
   times=1
   n+=1
   n2=0 
   print('请输入0~100的一个数字')
   while True:
      number_guess=int(input())
      if number_guess==number:
         print('恭喜你答对了！您一共答了%d轮'%times)
         cycle.append(times)
         n1=min(cycle)
         #print(cycle)
         for i in cycle:
            n2+=i
         mean_n2=n2/len(cycle)
         #print(n2,len(cycle))
         print('%s,你已玩了%d次，最少%d次猜中，平均%.2f次猜中'%(name,n,n1,mean_n2))
         answer=input('请问您还要继续游戏吗？输入y继续/其他退出')
         break
      if number_guess<number:
         times+=1
         print('您输入的数字偏小，请继续猜')
      if number_guess>number:
         times+=1
         print('您输入的数字偏大，请继续猜')
   if answer!='y':
      break

#Record
data={}
data['player']=name
data['total_times']=n
data['min_times']=n1
data_output=str('玩家名称:'+data['player']+'；总游戏轮数：'+str(data['total_times'])+'；最快游戏轮数：'+str(data['min_times']))
game_record=open(r'd:/game_one_user.txt','w')
game_record.write(data_output)
game_record.close()
