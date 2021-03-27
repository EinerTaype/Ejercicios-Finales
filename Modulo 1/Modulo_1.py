
# Ejercicio 1
a=input("Introduzca su nombre: ")

print(f"Hello, {a}")

a=input("Introduzca su nombre: ")

print(f"Hello, {a}")


# Problemas diversos

# problema 1
while(True):
    try:
        capital=float(input("ingrese cantidad a depositar"))
        break
    except:
        print("ha ocurrido un erro, introduce bien el número")
    
i=0.04

for t in range(1,4):
    a1=capital*((1+i)**t)
    print("la cantidad del primer año es: {}".format(a1))

balance=float(input("ingrese deposito"))
interes= 0.04

for i in range(3):
    balance=balance*(interes+1)
    balance=round(balance,2)
    print(f"El balance del año {i+1} es {balance}")


# problema 2

import math
print("dada la ecuacion cuadratica ax2+bx+c=0")
a=0
while a==0:
    a=float(input("ingreso coeficiente a: "))
    print("ingrese coeficiente diferente de 0")

b=float(input("ingreso coeficiente b: "))
c=float(input("ingreso coeficiente c: "))
determinante=b**2-4*a*c
if determinante<0:
    print("Ecuación no presenta solución real")
elif determinante==0:
    print("Presenta 1 única solución")
    x=-b/(2*a)
    print(f"solucion es: {x}")
elif determinante>0:
    x_1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
    x_2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
    print(f"la solucion 1 es: {x_1}")
    print(f"la solucion 2 es: {x_2}")
    
else:
    print("ingrese datos correctos")

def val_num(coef):
    while True:
        try:
            n=float(input(f"ingrese coeficiente {coef}: "))
            return n
        except:
            print("ha ocurrido un error, introduce bien el número")

a= val_num("a")
b=val_num("b")
c=val_num("c")