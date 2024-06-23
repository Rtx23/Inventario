class Proveedor: 
    def __init__(self, id_proveedor, nombre, telefono, email):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def to_dict(self):
        return {
            "id_proveedor": self.id_proveedor,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_proveedor"],
            dict_data["nombre"],
            dict_data["telefono"],
            dict_data["email"]
        )