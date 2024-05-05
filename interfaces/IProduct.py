from abc import abstractmethod
from abc import ABCMeta



class IProduct (metaclass=ABCMeta):
    
    @abstractmethod
    def Add(self):
        pass

     
    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def Edit(self):
        pass

    @abstractmethod
    def List(self):
        pass