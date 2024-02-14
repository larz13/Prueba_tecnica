#Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término.
def suma(numero, termino):
    suma = 0
    num = ''
    for i in range(1, termino + 1):
        num += str(numero)
        suma += (int(num))
    return suma


numero = int(input("ingrese numero: "))
termino = int(input("ingrese termino: "))
resultado = suma(numero,termino)
print("El resultado es ", resultado)

