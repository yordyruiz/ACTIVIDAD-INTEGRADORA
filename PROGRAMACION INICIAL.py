#módulos
from sum import suma
from maximo import mayor
from Minimo import minimo
from promedio import calcular_promedio  

#lista de numeros 
lista = []

for i in range(1,6):
    lista += [int(input("Ingresa el " + str(i) + ".º número entero: "))]


#Seleccion de operacion

opcion=int(input("""
----Operaciones disponibles----

1) Suma
2) Promedio
3) Máximo
4) Mínimo
Seleccione un número: """))


while True:

  if opcion==1:

    print("Eligió suma")
    suma(lista)
    break

  elif opcion==2:

    print("Eligió promedio")
    calcular_promedio(lista)
    break

  elif opcion==3:

    print("Eligió maximo")
    mayor(lista)
    break

  elif opcion==4:

    print("Eligió minimo")
    minimo(lista)
    break

  else:

    opcion=int(input(("Número incorrecto, ingrese nuevamente: ")))

 


    







#yordy ruiz
#Aula 1

