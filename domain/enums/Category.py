from enum import Enum

class Category(Enum):
    """Enum para representar las categorías de productos."""
    
    SMARTPHONE = 1
    COMPUTERS = 2 
    ELECTRONIC_ACCESSORY = 3
    DECORATIVE_ACCESSORY = 4
    
    @classmethod
    def get_category(cls, num: int):
        """Obtiene una categoría por su número de identificación.

        Args:
            num (int): El número de identificación de la categoría.

        Returns:
            Category: La categoría correspondiente al número de identificación.

        Raises:
            ValueError: Si no se encuentra una categoría con el número de identificación dado.
        """
        for category in cls:
            if category.value == num:
                return category
        raise ValueError("No such category exists")
