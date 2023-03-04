print("1. Realice un programa que pida al usuario un número entero positivo y después imprima en pantalla todos los números impares desde el uno hasta dicho número separado por comas.")
print("2. Realice un programa que calcule el número factorial de un número seleccionado por el usuario.")
print("3. Realice un programa que solicite un número al usuario, despues indique si es primo o no; además imprima los número primos hasta este número")
eje=1
while eje!=0:
    eje=int(input("Ingrese el numero del ejercicio que desea ejecutar(ingrese cero para terminar): "))
    if eje==1:
        num=int(input(" Ingrese un numero para saber el numero impares menores a este: "))
        n=1
        while n<=num:
            print(n,end=" , ")
            n+=2
    elif eje==2:
        x=int(input("Ingrese el número para saber el factorial: "))
        mul=1
        i=1
        for i in range(i,x+1):
            mul=i*mul
        print("El factorial es: ",mul)
    elif eje==3:
        y=int(input('Ingrese un numero para saber si es primo o no, y los primos menores: '))
        for i in range(2,int(y**0.5)+1):
            if y%i==0:
                print("El número ",y, " no es primo")
                break
            else: 
                print("El número ",y, "  es primo")
                break
        print('Y los primos menores son: ')
        for h in range(2,y):
            for o in range(2,h+1):
                if h%o==0:
                    break
                else:
                    print(h)
                    break
    else:
        print("Ingrese el 1,2,3 o 0 si desea terminar de visualizar el codigo escriba 0")
print("Fin del programa")


