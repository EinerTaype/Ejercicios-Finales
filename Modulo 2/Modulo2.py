# Problema 1

while (True):
    try:
        height=int(input("ingrese altura: "))
        break
    except:
         print("ha ocurrido un error, introduce bien el número")


contador=1
while contador<=height:
    print(" "*(height-contador)+"#"*contador)
    contador=contador+1
    
