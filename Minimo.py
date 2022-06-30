def minimo (lista):
   
   minimo=999

   for i in range (len(lista)):
      if lista[i]<minimo:
         minimo=lista[i]

   print("El menor número es:", minimo)