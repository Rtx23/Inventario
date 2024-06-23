class Cliente:
    def __init__(self, id_cliente, nombre, telefono, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["id_cliente"],
            dict_data["nombre"],
            dict_data["telefono"],
            dict_data["email"]
        )