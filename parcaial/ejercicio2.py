
n=int(input('Ingrese la cantidad de primos: '))
num=3
print('1')
print('2')
for h in range(1,n+1):
    for o in range(1,h+1):
        if h%o==0:
            pass
        else:
            print(h)
            num+=1
            break
