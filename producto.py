
class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_producto"],
            dict_data["nombre"],
            dict_data["descripcion"],
            dict_data["precio"],
            dict_data["stock"]
        )
