#P1
money = 88
if money>100:
  print('rich')
else:
  print('poor')


#P2
bingo = False
if bingo == False:
    print(True)
else:
    print(False)

b = 3
if b - 3:
    print(True)
else:
    print(False)

x = input('请输入内容')
if x:
    print(True)
else:
    print(False)

a = True
b = not a
print(b)
print(not b)
print(a == b)
print(a != b)
print(a and b)
print(a or b)
print(1<2 and b==True)

#P3
print('BMI cal')
height=float(input('请输入身高（cm）'))
weight=float(input('请输出体重（kg）'))
BMI=float(weight/((height/100)**2))
print('BMI=%.1f'%BMI)
if BMI<24:
  if BMI<18.5:
    print('您的体重偏轻。')
  else:
    print('您的体重正常。')
else:
  print('您的体重偏重。')
