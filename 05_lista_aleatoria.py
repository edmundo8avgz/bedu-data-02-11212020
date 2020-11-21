#Generar una lista con valores aleatorios

from random import randint

#lista vacia que contendra




lista_aleatoria = []
elementos = input('Cuantos elementos necesitas?')
elementos = int(elementos)

contador = 1

while contador <= elementos:
    #generamos valor aleatorio con randint
    matriz = randint(1,100)
    valor = matriz * elementos

    lista_aleatoria.append(valor)
    contador = contador + 1  

    print(f' -> {lista_aleatoria}')




   # if contador <= elementos:
    #    print('Contador es menor')
    #elif contador > elementos:
     #   print('Contador es mayor')

     
        
