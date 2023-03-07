""" import fexterna

def main():
    nombre = input('Escriba su nombre: ')
    fexterna.saludo(nombre)
    print('Fin del proceso', __name__)

if __name__=="__main__":
    main() """
from fexterna import fcn_factorial as f 
def main():
    n= int(input('Ingrese el numero de grupos: '))
    m= int (input("Ingrese el numero de muestra: "))
    result= ((f(n))/(f(m)*f(n-m)))
    print(f'El numero de combinaciones posibles es : {result}')

if __name__=="__main__":
    main()
