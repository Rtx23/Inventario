import os
from producto import Producto
from proveedor import Proveedor
from cliente import Cliente
from orden import Orden
from utils import write_data_json, read_data_json

# Definir la ruta de los archivos JSON
base_path = "data"
os.makedirs(base_path, exist_ok=True)
file_paths = {
    "productos": os.path.join(base_path, "productos.json"),
    "proveedores": os.path.join(base_path, "proveedores.json"),
    "clientes": os.path.join(base_path, "clientes.json"),
    "ordenes": os.path.join(base_path, "ordenes.json"),
}

def menu_principal():
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Gestionar Productos")
        print("2. Gestionar Proveedores")
        print("3. Gestionar Clientes")
        print("4. Gestionar Órdenes")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_productos()
        elif opcion == '2':
            menu_proveedores()
        elif opcion == '3':
            menu_clientes()
        elif opcion == '4':
            menu_ordenes()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_productos():
    productos = read_data_json(file_paths["productos"], Producto)
    
    while True:
        print("\nGestión de Productos")
        print("1. Agregar Producto")
        print("2. Ver Productos")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            for producto in productos:
                print(producto.__dict__)
        elif opcion == '3':
            write_data_json(file_paths["productos"], productos)
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_producto(productos):
    id_producto = int(input("ID del Producto: "))
    nombre = input("Nombre del Producto: ")
    descripcion = input("Descripción del Producto: ")
    precio = float(input("Precio del Producto: "))
    stock = int(input("Stock del Producto: "))
    
    nuevo_producto = Producto(id_producto, nombre, descripcion, precio, stock)
    productos.append(nuevo_producto)

def menu_proveedores():
    proveedores = read_data_json(file_paths["proveedores"], Proveedor)
    
    while True:
        print("\nGestión de Proveedores")
        print("1. Agregar Proveedor")
        print("2. Ver Proveedores")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_proveedor(proveedores)
        elif opcion == '2':
            for proveedor in proveedores:
                print(proveedor.__dict__)
        elif opcion == '3':
            write_data_json(file_paths["proveedores"], proveedores)
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_proveedor(proveedores):
    id_proveedor = int(input("ID del Proveedor: "))
    nombre = input("Nombre del Proveedor: ")
    telefono = input("Teléfono del Proveedor: ")
    email = input("Email del Proveedor: ")
    
    nuevo_proveedor = Proveedor(id_proveedor, nombre, telefono, email)
    proveedores.append(nuevo_proveedor)

def menu_clientes():
    clientes = read_data_json(file_paths["clientes"], Cliente)
    
    while True:
        print("\nGestión de Clientes")
        print("1. Agregar Cliente")
        print("2. Ver Clientes")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            for cliente in clientes:
                print(cliente.__dict__)
        elif opcion == '3':
            write_data_json(file_paths["clientes"], clientes)
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_cliente(clientes):
    id_cliente = int(input("ID del Cliente: "))
    nombre = input("Nombre del Cliente: ")
    telefono = input("Teléfono del Cliente: ")
    email = input("Email del Cliente: ")
    
    nuevo_cliente = Cliente(id_cliente, nombre, telefono, email)
    clientes.append(nuevo_cliente)

def menu_ordenes():
    ordenes = read_data_json(file_paths["ordenes"], Orden)
    
    while True:
        print("\nGestión de Órdenes")
        print("1. Agregar Orden")
        print("2. Ver Órdenes")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_orden(ordenes)
        elif opcion == '2':
            for orden in ordenes:
                print(orden.__dict__)
        elif opcion == '3':
            write_data_json(file_paths["ordenes"], ordenes)
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_orden(ordenes):
    id_orden = int(input("ID de la Orden: "))
    id_cliente = int(input("ID del Cliente: "))
    id_producto = int(input("ID del Producto: "))
    cantidad = int(input("Cantidad: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    
    nueva_orden = Orden(id_orden, id_cliente, id_producto, cantidad, fecha)
    ordenes.append(nueva_orden)

if __name__ == "__main__":
    menu_principal()
