""" n=int(input('Ingrese el número de primos que desea ver: '))
num=1
np=2
while num<=n:
  npr=True
  for i in range(2, int(np ** 0.5) +1):
    if np%i==0:
      npr=False
      break
  if npr:
    print(np,end=', ')
    num=num+1
  np+=1 """

num=int(input('Ingrese la cantidad de números que desea ver: '))
x=0
j=2
n=2
print('1')
while x<=num:
    div=n%j
    if div==0:
        if n==j:
            print(n)
            x+=1
        j=2
        n+=1
    else:
        j+=1
