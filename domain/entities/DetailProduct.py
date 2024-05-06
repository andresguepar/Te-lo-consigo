
from domain.entities.Product import Product
from domain.enums.Category import Category



class DetailProduct:
    def __init__(self,id = None, product = Product,name = None, description = None, price = None, category = Category, stock = None,):
        self.id = id
        self.product = product
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock