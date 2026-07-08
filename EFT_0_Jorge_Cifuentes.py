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

    return total_stock


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


def validar_precio(precio):
    return precio > 0


def agregar_producto(producto, inventario, codigo, nombre, categoria, precio, disponible, stock, vendidos):
    codigo = codigo.upper()
    disponible = disponible.lower()

    if not validar_codigo_nuevo(producto, inventario, codigo):
        return False
    
    if disponible == "s":
        disponible_booleano = True
    else:
        disponible_booleano = False
    
    producto[codigo] = [nombre, precio, categoria, disponible_booleano]
    inventario[codigo] = [stock, vendidos]

    return True


def eliminar_producto(producto, inventario, codigo):
    codigo = codigo.upper()

    if buscar_codigo(producto, inventario, codigo):
        del producto[codigo]
        del inventario[codigo]
        return True
    
    return False


def validar_texto(valor):
    return valor.strip() != "" #Validar texto


def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip() #Funcion para ingresar el intput
    
        if validar_texto(texto): #Validamos que no este vacio
            return texto
        else:
            print("El dato no puede estar vacio")


def ejecutar_stock_categoria(producto, inventario):
    categoria = leer_texto_no_vacio("Ingrese plataforma a consultar: ")

    total = stock_categoria(producto, inventario, categoria)

    print("El total de stock disponible es:", total)


def validar_entero(entero):
    return entero >= 0 #Para validar numero en stock y vendidos


def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) # "mensaje" colocara lo que escribamos en el print que lo llamemos
            return numero
        except ValueError:
            print("Debe ingresar un numero entero valido.")


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


def ejecutar_busqueda_precio(producto, inventario): # Segunda opcion del menu
    while True:
        p_min = leer_entero("ingrese precio minimo: ")

        if p_min >= 0:
            break
        else:
            print("El precio minimo debe ser mayor o igual a 0")

    while True:
        p_max = leer_entero("Ingrese precio maximo")

        if p_max >= 0:
            break
        else:
            print("El precio minimo debe ser mayor o igual a 0")
    
    if p_min > p_max:
        print("El precio minimo no puede ser mayor que el precio maximo")
        return
    
    resultados = buscar_precio(producto, inventario, p_min, p_max)

    if len(resultados) > 0:
        print("Los juegos encontrados son: ")
        print(resultados)
    else:
        print("No hay juegos en ese rango de precios")


def validar_disponible(disponible):
    disponible = disponible.lower()
    return disponible == "s" or disponible == "n"


def ejecutar_agregar_producto(producto, inventario):
    codigo = leer_texto_no_vacio("Ingrese codigo del juego: ").upper()

    if not validar_codigo_nuevo(producto, inventario, codigo):
        print("El codigo ya existe")
        return
    
    nombre = leer_texto_no_vacio("Ingrese titulo: ")
    categoria = leer_texto_no_vacio("Ingresar categoria: ")
    
    while True:
        precio = leer_entero("Ingrese precio: ")

        if validar_precio(precio):
            break
        else:
            print("El precio tiene que ser mayor a 0")
    
    while True:
        disponible = input("¿Esta disponible? s/n").lower().strip()

        if validar_disponible(disponible):
            break
        else:
            print("Debe ingresar s o n")
    
    while True:
        stock = leer_entero("Ingrese el stock del producto")

        if validar_entero(stock):
            break
        else:
            print("El stock debe ser mayor")

    while True:
        vendidos = leer_entero("Ingrese la cantidad vendida: ")

        if validar_entero(vendidos):
            break
        else:
            print("La cantidad vendida debe ser mayor o igual a 0")
    
    agregar = agregar_producto(
        producto,
        inventario,
        codigo,
        nombre,
        categoria,
        precio,
        disponible,
        stock,
        vendidos,
    )

    if agregar:
        print("Producto agregado")
    else:
        print("El codigo ya existe")








