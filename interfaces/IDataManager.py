from abc import ABC, abstractmethod
from domain.entities.DetailProduct import DetailProduct

class IDataManager(ABC):
    """Interfaz para definir métodos de gestión de datos."""

    @abstractmethod
    def load(self, product: DetailProduct):
        """Método abstracto para cargar datos.

        Args:
            product (DetailProduct): El detalle del producto que se cargará.

        Raises:
            NotImplementedError: Si el método no está implementado en la clase derivada.
        """
        pass
