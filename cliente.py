class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_cliente"],
            dict_data["nombre"],
            dict_data["direccion"],
            dict_data["telefono"]
        )
