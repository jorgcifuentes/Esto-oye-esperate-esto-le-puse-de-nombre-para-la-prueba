def mostrar_menu():
    print("========== MENU PRINCIPAL =========")
    print("1. Stock por categoria")
    print("2. Busqueda productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar producto")
    print("7. Salir")
    print("===================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 1 and opcion <=7:
                return opcion
            else:
                print("ERROR: Debe ingresar una opcion entre 1 y 7")
        except ValueError:
            print("Debe ingresar un numero entero")


def stock_categoria(categoria, productos, inventario):
    total_stock = 0

    for codigo in categoria:
        datos_categoria = categoria[codigo]
        inventario_categoria = datos_categoria[1]

        if inventario_categoria.lower() == productos.lower():
            if codigo in inventario:
                stock = inventario[codigo][1]
                total_stock = total_stock + stock

    return total_stock


def buscar_precio(p_min, p_max, productos, inventario):
    resultados = []

    for codigo in inventario:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio >= p_min and precio <= p_max and stock != 0:
            if codigo in productos:
                nombre = productos[codigo][0]
                resultados.append(nombre + "--" + codigo)
    
    resultados.sort()
    return resultados


def buscar_codigo(productos, inventario, codigo):
    codigo = codigo.upper()

    if codigo in productos and codigo in inventario:
        return True
    
    return False

def actualizar_precio(productos, inventario, codigo, nuevo_precio):
    codigo = codigo.upper

    if buscar_codigo(productos, inventario, codigo):
        














