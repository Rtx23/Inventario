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
            menu_entidad("productos", Producto)
        elif opcion == "2":
            menu_entidad("proveedores", Proveedor)
        elif opcion == "3":
            menu_entidad("clientes", Cliente)
        elif opcion == "4":
            menu_entidad("ordenes", Orden)
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_entidad(tipo_entidad, clase_entidad):
    datos = read_data_json(file_paths[tipo_entidad], clase_entidad)

    while True:
        print(f"\nMenú de {tipo_entidad.capitalize()}")
        print("1. Listar")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_entidades(datos, clase_entidad, tipo_entidad)  # Se pasa tipo_entidad
        elif opcion == "2":
            agregar_entidad(datos, clase_entidad)
        elif opcion == "3":
            actualizar_entidad(datos, clase_entidad)
        elif opcion == "4":
            eliminar_entidad(datos, clase_entidad)
            write_data_json(file_paths[tipo_entidad], datos)
        elif opcion == "5":
            write_data_json(file_paths[tipo_entidad], datos)
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        


def listar_entidades(entidades, clase_entidad, tipo_entidad):
    if clase_entidad == Producto:
        print(f"\n┌─────────────────────────────────────────────────────────────────────┐")
        print(f"│                        Listado de {tipo_entidad.capitalize()}                        │")
        print(f"├─────┬─────────────────────┬─────────────────────┬───────────┬───────┤")
        print(f"│ ID  │ Nombre              │ Descripción         │ Precio    │ Stock │")
        print(f"├─────┼─────────────────────┼─────────────────────┼───────────┼───────┤")
        for entidad in entidades:
            print(f"│ {str(entidad.id_producto).ljust(4)} │ {entidad.nombre.ljust(20)} │ {entidad.descripcion.ljust(20)} │ S/.{str(entidad.precio).ljust(9)} │ {str(entidad.stock).ljust(5)} │")
        print(f"└─────┴─────────────────────┴─────────────────────┴───────────┴───────┘")
    elif clase_entidad == Proveedor:
        print(f"\n┌──────────────────────────────────────────────────────────┐")
        print(f"│                    Listado de {tipo_entidad.capitalize()}                 │")
        print(f"├─────┬─────────────────────┬───────────────┬──────────────┤")
        print(f"│ ID  │ Nombre              │ Dirección     │ Teléfono     │")
        print(f"├─────┼─────────────────────┼───────────────┼──────────────┤")
        for entidad in entidades:
            print(f"│ {str(entidad.id_proveedor).ljust(4)} │ {entidad.nombre.ljust(20)} │ {entidad.direccion.ljust(13)} │ {entidad.telefono.ljust(12)} │")
        print(f"└─────┴─────────────────────┴───────────────┴──────────────┘")
    elif clase_entidad == Cliente:
        print(f"\n┌─────────────────────────────────────────────────────────┐")
        print(f"│                      Listado de {tipo_entidad.capitalize()}                   │")
        print(f"├─────┬─────────────────────┬───────────────┬──────────────┤")
        print(f"│ ID  │ Nombre              │ Di5rección     │ Teléfono     │")
        print(f"├─────┼─────────────────────┼───────────────┼──────────────┤")
        for entidad in entidades:
            print(f"│ {str(entidad.id_cliente).ljust(4)} │ {entidad.nombre.ljust(20)} │ {entidad.direccion.ljust(13)} │ {entidad.telefono.ljust(12)} │")
        print(f"└─────┴─────────────────────┴───────────────┴──────────────┘")
    elif clase_entidad == Orden:
        print(f"\n┌───────────────────────────────────────────────────────────────────┐")
        print(f"│                          Listado de {tipo_entidad.capitalize()}                        │")
        print(f"├─────┬───────────┬─────────────┬─────────────┬───────────┬──────────┤")
        print(f"│ ID  │ ID Cliente │ ID Producto │ Cantidad    │ Fecha     │")
        print(f"├─────┼───────────┼─────────────┼─────────────┼───────────┼──────────┤")
        for entidad in entidades:
            print(f"│ {str(entidad.id_orden).ljust(4)} │ {str(entidad.id_cliente).ljust(11)} │ {str(entidad.id_producto).ljust(11)} │ {str(entidad.cantidad).ljust(11)} │ {entidad.fecha.ljust(9)} │")
        print(f"└─────┴───────────┴─────────────┴─────────────┴───────────┴──────────┘")



def agregar_entidad(entidades, clase_entidad):
    if clase_entidad == Producto:
        id_entidad = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock del producto: "))

        nueva_entidad = clase_entidad(id_entidad, nombre, descripcion, precio, stock)
    elif clase_entidad == Proveedor:
        id_entidad = int(input("ID del proveedor: "))
        nombre = input("Nombre del proveedor: ")
        direccion = input("Dirección del proveedor: ")
        telefono = input("Teléfono del proveedor: ")

        nueva_entidad = clase_entidad(id_entidad, nombre, direccion, telefono)
    elif clase_entidad == Cliente:
        id_entidad = int(input("ID del cliente: "))
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")

        nueva_entidad = clase_entidad(id_entidad, nombre, direccion, telefono)
    elif clase_entidad == Orden:
        id_entidad = int(input("ID de la orden: "))
        id_cliente = int(input("ID del cliente: "))
        id_producto = int(input("ID del producto: "))
        cantidad = int(input("Cantidad: "))
        fecha = input("Fecha (YYYY-MM-DD): ")

        nueva_entidad = clase_entidad(id_entidad, id_cliente, id_producto, cantidad, fecha)
    else:
        print("Clase de entidad no válida.")

    entidades.append(nueva_entidad)
    write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
    print(f"{clase_entidad.__name__} agregado exitosamente.")



def eliminar_entidad(entidades, clase_entidad):
    id_entidad = int(input(f"ID del {clase_entidad.__name__.lower()} a eliminar: "))
    if clase_entidad == Producto:
        entidades = [e for e in entidades if not (isinstance(e, Producto) and e.id_producto == id_entidad)]
    elif clase_entidad == Proveedor:
        entidades = [e for e in entidades if not (isinstance(e, Proveedor) and e.id_proveedor == id_entidad)]
    elif clase_entidad == Cliente:
        entidades = [e for e in entidades if not (isinstance(e, Cliente) and e.id_cliente == id_entidad)]
    elif clase_entidad == Orden:
        entidades = [e for e in entidades if not (isinstance(e, Orden) and e.id_orden == id_entidad)]
    else:
        print("Clase de entidad no válida.")

    write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
    print(f"{clase_entidad.__name__} eliminado exitosamente.")

def actualizar_entidad(entidades, clase_entidad):
    if clase_entidad == Producto:
        id_entidad = int(input("ID del producto a actualizar: "))
        entidad = next((e for e in entidades if isinstance(e, Producto) and e.id_producto == id_entidad), None)
        if entidad:
            entidad.nombre = input("Nuevo nombre del producto: ")
            entidad.descripcion = input("Nueva descripción del producto: ")
            entidad.precio = float(input("Nuevo precio del producto: "))
            entidad.stock = int(input("Nuevo stock del producto: "))
            write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")
    elif clase_entidad == Proveedor:
        id_entidad = int(input("ID del proveedor a actualizar: "))
        entidad = next((e for e in entidades if isinstance(e, Proveedor) and e.id_proveedor == id_entidad), None)
        if entidad:
            entidad.nombre = input("Nuevo nombre del proveedor: ")
            entidad.direccion = input("Nueva dirección del proveedor: ")
            entidad.telefono = input("Nuevo teléfono del proveedor: ")
            write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
            print("Proveedor actualizado exitosamente.")
        else:
            print("Proveedor no encontrado.")
    elif clase_entidad == Cliente:
        id_entidad = int(input("ID del cliente a actualizar: "))
        entidad = next((e for e in entidades if isinstance(e, Cliente) and e.id_cliente == id_entidad), None)
        if entidad:
            entidad.nombre = input("Nuevo nombre del cliente: ")
            entidad.direccion = input("Nueva dirección del cliente: ")
            entidad.telefono = input("Nuevo teléfono del cliente: ")
            write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
            print("Cliente actualizado exitosamente.")
        else:
            print("Cliente no encontrado.")
    elif clase_entidad == Orden:
        id_entidad = int(input("ID de la orden a actualizar: "))
        entidad = next((e for e in entidades if isinstance(e, Orden) and e.id_orden == id_entidad), None)
        if entidad:
            entidad.id_cliente = int(input("Nuevo ID del cliente: "))
            entidad.id_producto = int(input("Nuevo ID del producto: "))
            entidad.cantidad = int(input("Nueva cantidad: "))
            entidad.fecha = input("Nueva fecha (YYYY-MM-DD): ")
            write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)
            print("Orden actualizada exitosamente.")
        else:
            print("Orden no encontrada.")
    else:
        print("Clase de entidad no válida.")

    write_data_json(file_paths[clase_entidad.__name__.lower() + 's'], entidades)

if __name__ == "__main__":
    menu_principal()
