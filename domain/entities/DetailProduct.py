from domain.enums.Category import Category


class DetailProduct:
    def __init__(self,id = None ,name = None, description = None, price = None, category = Category, stock = None,):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock