class Orden:
    def __init__(self, id_orden, id_cliente, id_producto, cantidad, fecha):
        self.id_orden = id_orden
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.fecha = fecha

    def to_dict(self):
        return {
            "id_orden": self.id_orden,
            "id_cliente": self.id_cliente,
            "id_producto": self.id_producto,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_orden"],
            dict_data["id_cliente"],
            dict_data["id_producto"],
            dict_data["cantidad"],
            dict_data["fecha"]
        )
