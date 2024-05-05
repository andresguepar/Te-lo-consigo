from abc import ABC, abstractmethod

from domain.entities.DetailProduct import DetailProduct

class IDataManager(ABC):
     
     @abstractmethod
     def load(self,product: DetailProduct):
        pass