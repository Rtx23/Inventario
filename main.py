from producto import Producto
from proveedor import Proveedor
from cliente import Cliente
from orden import Orden
from utils import write_data_json, read_data_json

file_paths = {
    "productos": "data/productos.json",
    "proveedores": "data/proveedores.json",
    "clientes": "data/clientes.json",
    "ordenes": "data/ordenes.json"
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

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_proveedores()
        elif opcion == "3":
            menu_clientes()
        elif opcion == "4":
            menu_ordenes()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_productos():
    productos = read_data_json(file_paths["productos"], Producto)

    while True:
        print("\nMenú de Productos")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for producto in productos:
                print(producto.to_dict())
        elif opcion == "2":
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock del producto: "))

            nuevo_producto = Producto(id_producto, nombre, descripcion, precio, stock)
            productos.append(nuevo_producto)
            write_data_json(file_paths["productos"], productos)
            print("Producto agregado exitosamente.")
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            producto = next((p for p in productos if p.id_producto == id_producto), None)
            if producto:
                producto.nombre = input("Nuevo nombre del producto: ")
                producto.descripcion = input("Nueva descripción del producto: ")
                producto.precio = float(input("Nuevo precio del producto: "))
                producto.stock = int(input("Nuevo stock del producto: "))
                write_data_json(file_paths["productos"], productos)
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            productos = [p for p in productos if p.id_producto != id_producto]
            write_data_json(file_paths["productos"], productos)
            print("Producto eliminado exitosamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_proveedores():
    proveedores = read_data_json(file_paths["proveedores"], Proveedor)

    while True:
        print("\nMenú de Proveedores")
        print("1. Listar proveedores")
        print("2. Agregar proveedor")
        print("3. Actualizar proveedor")
        print("4. Eliminar proveedor")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for proveedor in proveedores:
                print(proveedor.to_dict())
        elif opcion == "2":
            id_proveedor = int(input("ID del proveedor: "))
            nombre = input("Nombre del proveedor: ")
            direccion = input("Dirección del proveedor: ")
            telefono = input("Teléfono del proveedor: ")

            nuevo_proveedor = Proveedor(id_proveedor, nombre, direccion, telefono)
            proveedores.append(nuevo_proveedor)
            write_data_json(file_paths["proveedores"], proveedores)
            print("Proveedor agregado exitosamente.")
        elif opcion == "3":
            id_proveedor = int(input("ID del proveedor a actualizar: "))
            proveedor = next((p for p in proveedores if p.id_proveedor == id_proveedor), None)
            if proveedor:
                proveedor.nombre = input("Nuevo nombre del proveedor: ")
                proveedor.direccion = input("Nueva dirección del proveedor: ")
                proveedor.telefono = input("Nuevo teléfono del proveedor: ")
                write_data_json(file_paths["proveedores"], proveedores)
                print("Proveedor actualizado exitosamente.")
            else:
                print("Proveedor no encontrado.")
        elif opcion == "4":
            id_proveedor = int(input("ID del proveedor a eliminar: "))
            proveedores = [p for p in proveedores if p.id_proveedor != id_proveedor]
            write_data_json(file_paths["proveedores"], proveedores)
            print("Proveedor eliminado exitosamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_clientes():
    clientes = read_data_json(file_paths["clientes"], Cliente)

    while True:
        print("\nMenú de Clientes")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for cliente in clientes:
                print(cliente.to_dict())
        elif opcion == "2":
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")

            nuevo_cliente = Cliente(id_cliente, nombre, direccion, telefono)
            clientes.append(nuevo_cliente)
            write_data_json(file_paths["clientes"], clientes)
            print("Cliente agregado exitosamente.")
        elif opcion == "3":
            id_cliente = int(input("ID del cliente a actualizar: "))
            cliente = next((c for c in clientes if c.id_cliente == id_cliente), None)
            if cliente:
                cliente.nombre = input("Nuevo nombre del cliente: ")
                cliente.direccion = input("Nueva dirección del cliente: ")
                cliente.telefono = input("Nuevo teléfono del cliente: ")
                write_data_json(file_paths["clientes"], clientes)
                print("Cliente actualizado exitosamente.")
            else:
                print("Cliente no encontrado.")
        elif opcion == "4":
            id_cliente = int(input("ID del cliente a eliminar: "))
            clientes = [c for c in clientes if c.id_cliente != id_cliente]
            write_data_json(file_paths["clientes"], clientes)
            print("Cliente eliminado exitosamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_ordenes():
    ordenes = read_data_json(file_paths["ordenes"], Orden)

    while True:
        print("\nMenú de Órdenes")
        print("1. Listar órdenes")
        print("2. Agregar orden")
        print("3. Actualizar orden")
        print("4. Eliminar orden")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for orden in ordenes:
                print(orden.to_dict())
        elif opcion == "2":
            id_orden = int(input("ID de la orden: "))
            id_cliente = int(input("ID del cliente: "))
            id_producto = int(input("ID del producto: "))
            cantidad = int(input("Cantidad: "))
            fecha = input("Fecha (YYYY-MM-DD): ")

            nueva_orden = Orden(id_orden, id_cliente, id_producto, cantidad, fecha)
            ordenes.append(nueva_orden)
            write_data_json(file_paths["ordenes"], ordenes)
            print("Orden agregada exitosamente.")
        elif opcion == "3":
            id_orden = int(input("ID de la orden a actualizar: "))
            orden = next((o for o in ordenes if o.id_orden == id_orden), None)
            if orden:
                orden.id_cliente = int(input("Nuevo ID del cliente: "))
                orden.id_producto = int(input("Nuevo ID del producto: "))
                orden.cantidad = int(input("Nueva cantidad: "))
                orden.fecha = input("Nueva fecha (YYYY-MM-DD): ")
                write_data_json(file_paths["ordenes"], ordenes)
                print("Orden actualizada exitosamente.")
            else:
                print("Orden no encontrada.")
        elif opcion == "4":
            id_orden = int(input("ID de la orden a eliminar: "))
            ordenes = [o for o in ordenes if o.id_orden != id_orden]
            write_data_json(file_paths["ordenes"], ordenes)
            print("Orden eliminada exitosamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
