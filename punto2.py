import math 
cateto1=float(input("Ingrese el valor del primer cateto: "))
cateto2=float(input("Ingrese el valor del segundo cateto: "))
if cateto1>0 and cateto2>0:
    h=math.sqrt((cateto1**2)+(cateto2**2))
    print("La hipotenusa de su triangulo es: ",h)
else:
    print("Los catetos deben ser mayor a cero")
