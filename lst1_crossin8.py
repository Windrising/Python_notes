#P1
data={'one':1,'two':2,'three':3}
data['two']=4
print(data)

#P2
sentence='Beautiful is better than ugly Explicit is better than implicit Simple is better than complex Complex is better than complicated Flat is better than nested Sparse is better than dense'
word=sentence.split()
sta={}
for i in word:
  if i in sta:
    sta[i]+=1
  else:
    sta[i]=1
print(sta)
