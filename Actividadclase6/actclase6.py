
def saludo(nombre):
    print('Hola ',nombre)
    return
def factorial(x):
    mul=1
    for i in range(1,x+1,1):
        mul=mul*i
    return mul

print('1.Desarrolle una función llamada Saludo, en donde se solicite el nombre al usuario y cada vez que se invoque dicha función, se imprima por pantalla Hola <Nombre_Usuario> ')
print('2.Desarrolle un programa para calcular el numero de combinaciones binomiales que pueden darse en un conjunto de n elementos organizados en r número de muestras sin orden.')
eje=1
while eje!=0:
    eje=int(input("Ingrese el numero del ejercicios que desea realizar(ingrese cero para ternminar): "))
    if eje==1:
        name=input("Ingrese su nombre: ")
        saludo(name)
    elif eje==2:
        n=int(input("Ingrese los elementos organizados: "))
        r=int(input("Ingrese el numero de muestras sin ordenar: "))
        x=n-r
        com=factorial(n)/(factorial(r)*factorial(x))
        print('Las posibles combinaciones son: ',com)
    elif eje==0:
        break
    else:
        print("Ingrese el número 1 si desea ver el ejercicio 1 o ingrese el número 2 si desea ver el ejercicio 2 o ingrese 0 para terminar el proceso ")
print('Fin del programa')

    

