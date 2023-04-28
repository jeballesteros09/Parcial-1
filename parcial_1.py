import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('inventario.db')
c = conn.cursor()

# Creación de la tabla
c.execute('''CREATE TABLE IF NOT EXISTS productos
             (id_categoria INTEGER, nombre_producto TEXT, cantidad INTEGER, precio REAL)''')


def agregar_producto():
    id_producto = int(input("Ingrese el ID del del producto: "))
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))

    c.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (id_producto, nombre_producto, cantidad, precio))
    conn.commit()

    print("El producto ha sido agregado al inventario.")


def editar_producto():
    id_producto = int(input("Ingrese el ID del producto que desea editar: "))

    # Consulta para obtener los datos actuales del producto
    c.execute("SELECT * FROM productos WHERE rowid = ?", (id_producto,))
    producto = c.fetchone()

    if producto:
        print(f"Datos actuales del producto: {producto}")

        # Solicita los nuevos datos para el producto
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad de productos: "))
        precio = float(input("Ingrese el precio del producto: "))

        # Actualiza los datos del producto en la base de datos
        c.execute("UPDATE productos SET nombre_producto = ?, cantidad = ?, precio = ? WHERE rowid = ?",
                  (nombre_producto, cantidad, precio, id_producto))
        conn.commit()

        print("El producto ha sido actualizado en el inventario.")
    else:
        print("El ID del producto ingresado no existe.")


def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))

    # Consulta para obtener los datos del producto a eliminar
    c.execute("SELECT * FROM productos WHERE rowid = ?", (id_producto,))
    producto = c.fetchone()

    if producto:
        c.execute("DELETE FROM productos WHERE rowid = ?", (id_producto,))
        conn.commit()

        print("El producto ha sido eliminado del inventario.")
    else:
        print("El ID del producto ingresado no existe.")


def buscar_producto():
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")

    # Consulta para obtener los datos del producto a buscar
    c.execute("SELECT * FROM productos WHERE nombre_producto = ?", (nombre_producto,))
    producto = c.fetchone()

    if producto:
        print(f"Datos del producto encontrado: {producto}")
    else:
        print("El producto ingresado no existe en el inventario.")


def ver_inventario():
    # Consulta para obtener todos los productos del inventario
    c.execute("SELECT * FROM productos")
    productos = c.fetchall()

    if productos:
        for producto in productos:
            print(producto)
    else:
        print("El inventario está vacío.")


# Menú principal
while True:
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Ver inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        editar_producto()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        buscar_producto()
    elif opcion == '5':
        ver_inventario()
    elif opcion == '6':
        break
    else:
        print("Opcion invalida.")
