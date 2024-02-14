#Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las
#siguientes condiciones:
#1. El número debe ser divisible por cinco.
#2. Si el número es mayor que 600, no se incluye en la salida.
#3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.

def listafiltro(lista):
    listaFinal = []
    for numero in lista:
        if numero % 5 == 0:
            if numero <= 600:
                listaFinal.append(numero)
            elif numero > 1000:
                return listaFinal
    return listaFinal

#entrada1 = [24,150,300,660,295,1050,50]
#ntrada2 = [110, 720, 307, 555, 1095, 12, 300, 1000]
#resultado = listafiltro(entrada2)
#print("Números filtrados:", resultado)

#con este fragmento el usuario puede ingresar cualquier cantidad de valores SEPARADOS por , y se aplicara el fitrado                
numeros = input("Ingrese una lista de números separados por comas: ")
lista = [int(numero) for numero in numeros.split(',')]
resultado = listafiltro(lista)
print("La lista resultante es: ", resultado)
