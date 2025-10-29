#EJERCICIO 1 :


#EJERCICIO 2:

def esPar(numero):
    if numero % 2 == 0:
        return True
    else: False   

numero = int(input("ingrese un numero para saber si es par o no"))
print("es el numero par?",esPar(numero))
