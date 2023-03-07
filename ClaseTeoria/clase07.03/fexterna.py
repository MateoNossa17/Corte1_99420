""" def saludo(nombre):
    print(f'Hola {nombre}')
    print('Funcion: ',__name__)


if __name__=='__main__':
    saludo('Juan')
 """
def fcn_factorial(x):
    mul=1
    for i in range(2,x+1):
        mul*=i
    return mul

