class Proveedor:
    def __init__(self, id_proveedor, nombre, direccion, telefono):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return {
            "id_proveedor": self.id_proveedor,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_proveedor"],
            dict_data["nombre"],
            dict_data["direccion"],
            dict_data["telefono"]
        )
