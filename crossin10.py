#P1
def func(x):
    print (x)
    return x+1

x = 2
print (func(x)) #输出2 & 3

#P2
def func(param):
  return param*2

p=func(20)
print(p)

#P3
def combine(a,b):
  return sorted(a+b)

print(combine([1,5,3],[2,6,7,4]))
