# Prueba_tecnica
Prueba tecnica - Globaltek - Developer Jr
**************************************************************************************************************************************
DESCRIPCION DE LOS PROGRAMAS
1Ejercicio------------------------------------------------------------------------------------------------------------------------------------
Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término. Ejemplos:

Entrada : numero=3, terminos=5
Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)
Entrada : numero=5, terminos=3
Salida : 615 #(5 + 55 + 555)

2Ejercicio------------------------------------------------------------------------------------------------------------------------------------
Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las
siguientes condiciones:
1. El número debe ser divisible por cinco.
2. Si el número es mayor que 600, no se incluye en la salida.
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.

Ejemplos:
Entrada : [24, 150, 300, 660, 295, 1050, 50]
Salida : [150, 300, 295]
Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
Salida : [110, 555]

3Ejercicio------------------------------------------------------------------------------------------------------------------------------------
Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz
de salida (no importa el orden). Ejemplos:
Entrada : list = [12, 25, 1, 1, 7, 25]
Salida : [[12], [7], [25, 25], [1, 1]]
Entrada : list = [6, 7, 8, 9]
Salida : [[6], [7], [8], [9]]

4Ejercicio------------------------------------------------------------------------------------------------------------------------------------
En un negocio reciben periódicamente productos para la venta, se requiere desarrollar un programa de consola (o
terminal) que cumpla con los siguientes requerimientos:
1. Se requiere organizar el inventario en los siguientes grupos: dairy, cleaning y grain.
2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la
misma posición, como en el siguiente ejemplo:
dairy_products = [“Fairlife Milk”, “Alta Dena Milk”, “Queensland Butter”]
dairy_stock = [28, 36, 50]
En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.
3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo
al que pertenece.
4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe
actualizar el número de existencias sumando la nueva cantidad.
5. El programa debe permitir visualizar todo el inventario de productos y existencias

**************************************************************************************************************************************
PASOS PARA EJECUTAR CADA PROGRAMA
los pasos necesarios para compilar y ejecutar los programas en Python:

Instala Python:------------------------------------------------------------------------------------------------------------------------------------
Si aún no tienes Python instalado en tu sistema, necesitarás descargarlo e instalarlo desde el sitio web oficial de Python (https://www.python.org/). Asegúrate de marcar la casilla que dice "Agregar Python X.X al PATH" durante la instalación para poder ejecutar Python desde la línea de comandos.

Clona o Descarga el repositorio
una vez descargado o clonado acceda a la carpeta principal y abra su contenido desde su editor de texto preferido, tambien puedes arratrar la carpeta hacia el editor y este se encargara de mostrar el contenido de la carpeta
**************************************************************************************************************************************
TAMBIEN PUEDES:
    Abre un editor de texto:------------------------------------------------------------------------------------------------------------------------------------
    Utiliza tu editor de texto o entorno de desarrollo integrado (IDE) preferido para escribir el código del programa que desee, en mi caso uso Visual Studio Code. una vez abierto crear un archivo con el nombre que desees y no olvides guardarlo con la extension ".py"
    
    Escribe el código:------------------------------------------------------------------------------------------------------------------------------------
    Copia y pega el código del programa de inventario en un archivo nuevo en tu editor de texto.

**************************************************************************************************************************************

PARA COMPILAR EL CODIGO:

Puedes hacerlo directamente desde el editor de texto, solo valida la tecla con la cual puedes compilar en el editor que estes usando, en mi caso es F5 o tambien puedes abrir una terminal y accediendo a la direccion donde esta ubicada el archivo guardado y una vez en el directorio correcto, simplemente escribe python seguido del nombre del archivo que creaste. Por ejemplo: python nombre.py
