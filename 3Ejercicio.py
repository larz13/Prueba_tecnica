#Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz de salida

from itertools import groupby

def agrupar_elementos(lista):
    matriz = []
    lista_ordenada = sorted(lista)
    for key, group in groupby(lista_ordenada):
        sublista = list(group)
        matriz.append(sublista)
    return matriz

entrada1 = [12, 25, 1, 1, 7, 25]
entrada2 =  [6, 7, 8, 9]

matriz_salida = agrupar_elementos(entrada2)
print("Matriz de salida:", matriz_salida)



