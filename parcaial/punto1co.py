n=int(input('Ingrese el número: '))
d5=0
i5=0
while n!=0:
    x=(n//10)
    dig=n-(x*10)
    n=x
    if dig==5:
        print('salto')
        i5+=1
    else:
        print(dig)
        d5+=1
print(f'digitos diferentes de 5:{d5}')
print(f'digitos iguales a 5: {i5}')
    