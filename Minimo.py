def minimo (lista):
   
   minimo=0

   for i in range (len(lista)):
      if lista[i]<minimo:
         minimo=lista[i]

   print("El mayor número es:", minimo)