#Ciclo for:
#shit+alt+a

""" print("Seleccione una de las siguinetres pbciones: ")
print("1. for in renge(finla)")
print("2. for in renge(inicio, final)")
print("3. for in renge(inicio, final, paso)")
opc=int(input("Escoja una opcion"))
if opc==1:
    for i in range(10):
        print(i+1)
elif opc==2:
    for i in range(1,11):
        print(i)
else:
    for i in range(1,10,2):
        print(i)
 """

#FUNCIONES

""" def suma(a,b):
    s=a+b
    return s
def imprimir(nombre):
    print(f'{nombre} su resultado es: ')
nombre=input('Ingrese su nombre: ')
n='si'
while n=='si':
    a=int(input('Ingrese un numero: '))
    b=int(input('Ingrese un numero: '))
    res=suma(a,b)
    imprimir(nombre)
    print(res)   
    n=input('Quiere sumar otro numero?si/no ') 
 """
""" print(suma(2,3)) """
import math
"""
def area(r):
    a=math.pi*(r**2)
    return a
def volumen(r,h):
    v=area(r)*h
    return v
r=float(input('Ingrese le valor del radio: '))
h=float(input('Ingrese la altura: ')) """
""" print(f'el area es {area(r)} y el volumen es: {volumen(r,h)}') """

resultado=math.factorial(4)/(math.factorial(2)*math.factorial(4-2))
print(resultado)