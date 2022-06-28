def calcular_promedio (lista_numeros):
    suma= 0
    for numero in lista_numeros:
        suma = suma + numero
    cantidad = len(lista_numeros)
    resultado = suma / cantidad 
    print("el promedio es :", resultado)