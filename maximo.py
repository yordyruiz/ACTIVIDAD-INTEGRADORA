def mayor(lista):
   
    maximo=-999

    for i in range (len(lista)):
     if lista[i]>maximo:
        maximo=lista[i]

    print("El mayor número es:", maximo)