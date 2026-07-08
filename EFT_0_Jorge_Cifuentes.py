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


def stock_categoria(productos, inventario, categoria):
    total_stock = 0

    for codigo in productos:
        datos_producto = productos[codigo]
        categoria_producto = datos_producto[1]

        if categoria_producto.lower() == categoria.lower():
            if codigo in productos:
                stock = inventario[codigo][0] # indice 0 = stock
                total_stock += stock

    print(f"{total_stock}")


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
    codigo = codigo.upper()

    if buscar_codigo(productos, inventario, codigo):
        productos[codigo][2] = nuevo_precio
        return True

    return False


def validar_codigo_nuevo(productos, inventario, codigo):
    codigo = codigo.upper()
    return codigo != "" and codigo not in productos and codigo not in inventario


def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_disponible(disponible):
    disponible = disponible.lower()
    return disponible == "s" or disponible == "n"

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0


def agregar_producto(producto, inventario, codigo, nombre, categoria, precio, disponible, stock, vendidos):
    codigo = codigo.upper()
    disponible = disponible.lower()

    if validar_codigo_nuevo(producto, inventario, codigo):
        return False
    
    if disponible == "s":
        disponible_booleano = True
    else:
        disponible_booleano = False
    
    producto[codigo] = [nombre, precio, categoria, disponible_booleano]
    inventario[codigo] = [stock, vendidos]

    return True


def eliminar_producto(producto, inventario, codigo):
    codigo = codigo.upper

    if buscar_codigo(producto, inventario, codigo):
        del producto[codigo]
        del inventario[codigo]
        return True
    
    return False












