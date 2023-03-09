def ejer2(n):     
    n=int(input('Ingrese un numero de 4 a 10 digitos: '))
    igualesa7=0
    dis7=0
    x=10
    for i in range(x,1000000):
        divi=n/i
        r=int(divi)*i
        rs=n-r
        if rs==7:
            print('salto')
            dis7+=1
        else:
            print(rs)
            igualesa7+=1
        x=x*10
        print('Digitos iguales a siete: ',igualesa7)
        print('Digitos diferesntes a siete: ',dis7)

        