#Realice un programa donde se soliciten dos números al usuario, después se 
# de como resultado el residuo y el cociente de la división entre <n1> y <n2>.
n1=float(input("Ingrese el valor de primer número: "))
n2=float(input("Ingrese el valor de segundo número: "))
if n1>0 and n2>0:
    d=n1/n2
    r=n1%n2
    print("La divicion entres los valores da: ",d," y el residuo de la misma es: ",r)
else:
    print("Escriba valores mayores a cero")

#Realice un programa que calcule el índice de masa corporal de una persona, 
#donde le solicite al usuario la estatura en cm y el peso en Kg. Después 
#imprima como resultado el índice de masa corporal mediante un mensaje que 
#diga “Su IMC es <valor>” redondeado con dos decimales. 
kg=float(input("Ingresa el valor de su peso en kilogramo: "))
cm=float(input("Ingrese el su altura en centimetros: "))
if kg>0 and cm>0:
    m=cm/100
    imc=kg/(m**2)
    print('Su IMC es: ',imc)
else:
    print("Ingrese valores mayores a cero")

#Realice un programa donde se solicite al usuario escribir el precio final de un 
#artículo o producto, con el que después calculará e imprimirá en pantalla el 
#valor del IVA y el valor bruto (precio antes de IVA) del artículo o producto. 
va=float(input("Ingrese el precio del producto: "))
if va>0:
    iva=va*(19/100)
    pb=va-iva
    print("El valor del IVA en el producto es: ",iva," y el precio bruto es: ",pb)
else:
    print("El valor del producto debe ser mayor a cero.")

#Realice un programa que permita calcular el costo anual del consumo de 
#combustible de un vehículo, si el usuario ingresa la distancia recorrida (Km) 
#anual, el consumo de combustible (L / 100Km) anual y el costo promedio 
#anual del combustible por litros recorridos ($ / L)
dr=float(input("Ingrese la distacia recorrida anualmente en kilometros: "))
cc=float(input("Ingrese el consumo de combustible cada 100Km en litros: "))
cp=float(input("Ingrese el valor promedio del combustible por litros: "))
if dr>0 and cc>0 and cp>0:
    litros=dr*(cc/100)
    coste=litros*cp
    print("El costo anual del consumo de combustible: ",coste)
else:
    print("Los valores deben ser mayores a cero")