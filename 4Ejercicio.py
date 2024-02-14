dairy_products = ["Leche", "Huevos", "Mantequilla"]
dairy_stock = [28, 36, 50]

cleaning_products = ["Jabon", "clorox", "Detergente"]
cleaning_stock = [20, 15, 30]

grain_products = ["Arroz", "Lentejas", "Frijoles"]
grain_stock = [40, 25, 35]

def add_update(product_name, quantity, group):
    if group == 'dairy':
        products = dairy_products
        stock = dairy_stock
    elif group == 'cleaning':
        products = cleaning_products
        stock = cleaning_stock
    elif group == 'grain':
        products = grain_products
        stock = grain_stock
    else:
        print("\U000026A0 Grupo no válido\n")
        return

    if product_name in products:
        index = products.index(product_name)
        stock[index] += quantity
    else:
        products.append(product_name)
        stock.append(quantity)

def show_inventory():
    print("\nInventario:")
    print("--------------------------------------")
    print("Dairy:")
    for i in range(len(dairy_products)):
        print(f"{i+1}{") "}{dairy_products[i]}: {dairy_stock[i]}")
    print("--------------------------------------")
    print("Cleaning:")
    for i in range(len(cleaning_products)):
        print(f"{i+1}{") "}{cleaning_products[i]}: {cleaning_stock[i]}")
    print("--------------------------------------")
    print("Grain:")
    for i in range(len(grain_products)):
        print(f"{i+1}{") "}{grain_products[i]}: {grain_stock[i]}")
        
    input("\nPresiona Enter para volver al menú principal")

while True:
    print("+----------------------------------------+")
    print("\t1. Registrar nuevo producto")
    print("\t2. Mostrar inventario")
    print("\t3. Salir")
    print("+----------------------------------------+")
    option = input("Seleccione una opción: ")

    if option == '1':
        product_name = input("Nombre del producto: ").capitalize()
        quantity = int(input("Cantidad: "))
        group = input("Grupo (dairy, cleaning, grain): ")
        add_update(product_name, quantity, group)
    elif option == '2':
        show_inventory()
    elif option == '3':
        print("¡Hasta luego!\U0001F44B")
        break
    else:
        print("Opción no válida")