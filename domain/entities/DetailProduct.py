
from domain.entities.Product import Product



class DetailProduct:
    def __init__(self,id = None ,name = Product.name, description = None, price = None, category = Product.category, stock = None,):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock