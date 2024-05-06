from domain.enums.Type import Type

class User:
    """Clase para representar un usuario.

    Attributes:
        id (int): El identificador único del usuario.
        name (str): El nombre del usuario.
        email (str): El correo electrónico del usuario.
        phone (str): El número de teléfono del usuario.
        type (Type): El tipo de usuario (ejemplo: Type.REGULAR, Type.ADMIN).
    """

    def __init__(self, id=None, name=None, phone=None, email=None, type=Type):
        """Inicializa un nuevo objeto Usuario.

        Args:
            id (int, optional): El identificador único del usuario.
            name (str, optional): El nombre del usuario.
            phone (str, optional): El número de teléfono del usuario.
            email (str, optional): El correo electrónico del usuario.
            type (Type, optional): El tipo de usuario (por defecto es Type).
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.type = type
