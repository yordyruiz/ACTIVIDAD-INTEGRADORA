#módulos
from maximo import mayor

#lista de numeros 
lista = []

for i in range(1,6):
    lista += [int(input("Ingresa el " + str(i) + ".º número entero: "))]

#Funcion suma 
def suma(lista):

    total = 0

    for i in lista:
        total += i

    print("El resultado de la suma de todos los elementos es", total)


mayor(lista)

#yordy ruiz
#Aula 1

